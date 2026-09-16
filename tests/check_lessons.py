#!/usr/bin/env python3
"""Cross-check each lesson's hardcoded demo tables against its data files.

Stdlib only (csv/re/sys/pathlib) - no third-party packages.
Each check_<lesson>() reads the lesson's SKILL.md and its assets/*.csv (or .md)
files from scratch, recomputes what the "Present it like this" table should
say, and compares that against what is actually written in SKILL.md.
"""
import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"


def read_csv_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_text(path):
    return path.read_text(encoding="utf-8")


def is_declining(values):
    """True if values strictly decrease at every step (e.g. [63, 60, 55])."""
    return all(values[i] > values[i + 1] for i in range(len(values) - 1))


def extract_between(text, start_marker, end_marker):
    start = text.index(start_marker)
    end = text.index(end_marker, start + len(start_marker))
    return text[start:end]


def parse_md_table(block):
    """Parse a markdown table into a list of dicts keyed by header cell."""
    lines = [l.strip() for l in block.splitlines() if l.strip().startswith("|")]
    if len(lines) < 2:
        return []
    headers = [c.strip() for c in lines[0].strip("|").split("|")]
    rows = []
    for line in lines[2:]:  # skip header + separator row
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r"\.*", c) for c in cells):
            continue  # skip "..." placeholder rows, they are not real claims
        rows.append(dict(zip(headers, cells)))
    return rows


def num_seq(text):
    """Extract the first '63→60→55' style number sequence from free text."""
    m = re.search(r"\d{1,3}(?:→\d{1,3}){2,3}", text)
    if not m:
        return None
    return [int(x) for x in m.group(0).split("→")]


# ---------------------------------------------------------------------------
# Lesson 1-1
# ---------------------------------------------------------------------------

def check_1_1():
    issues = []
    base = SKILLS_DIR / "start-1-1"
    skill = read_text(base / "SKILL.md")
    assets = base / "assets/horizon-academy"

    scores = {
        r["學號"]: [int(r["月考一"]), int(r["月考二"]), int(r["月考三"])]
        for r in read_csv_rows(assets / "exam-scores.csv")
    }
    survey = {r["學號"]: r for r in read_csv_rows(assets / "parent-survey.csv")}

    declining = {sid for sid, vals in scores.items() if is_declining(vals)}

    # Rule stated in SKILL.md Step 3: declining AND (satisfaction <= 3 OR
    # parent left a comment at all).
    rule_priority = set()
    for sid in declining:
        row = survey[sid]
        satisfaction = int(row["滿意度(1-5)"])
        comment = row["開放填答"].strip()
        if satisfaction <= 3 or comment:
            rule_priority.add(sid)

    block = extract_between(skill, "**本週優先關注**", "**下週留意**")
    table_priority = {r["學號"] for r in parse_md_table(block)}

    if rule_priority != table_priority:
        missing = sorted(rule_priority - table_priority)
        extra = sorted(table_priority - rule_priority)
        issues.append(
            "1-1 Step3「本週優先關注」表格與規則算出的結果不一致："
            f"規則（成績連續下滑 + 滿意度<=3 或有家長留言）算出 {sorted(rule_priority)}"
            f"（共 {len(rule_priority)} 位），示範表格只列出 {sorted(table_priority)}"
            f"（共 {len(table_priority)} 位）。"
            + (f" 表格漏列：{missing}。" if missing else "")
            + (f" 表格多列：{extra}。" if extra else "")
        )
    return issues


# ---------------------------------------------------------------------------
# Lesson 2-1
# ---------------------------------------------------------------------------

def check_2_1():
    issues = []
    base = SKILLS_DIR / "start-2-1"
    skill = read_text(base / "SKILL.md")
    assets = base / "assets/horizon-academy"

    oct_scores = {
        r["學號"]: [int(r["月考一"]), int(r["月考二"]), int(r["月考三"]), int(r["本月測驗"])]
        for r in read_csv_rows(assets / "exam-scores-oct.csv")
    }
    watchlist = read_csv_rows(assets / "priority-watchlist.csv")

    m = re.search(r"張志豪.*?成績趨勢（(\d{1,3}(?:→\d{1,3}){2,3})）", skill, re.S)
    if not m:
        issues.append("2-1：找不到 Step2 引用張志豪成績趨勢的文字，SKILL.md 結構可能變了")
    else:
        cited = [int(x) for x in m.group(1).split("→")]
        if cited != oct_scores["S019"]:
            issues.append(
                f"2-1 Step2 引用張志豪成績趨勢 {cited}，與 exam-scores-oct.csv 的 {oct_scores['S019']} 不一致"
            )

    m = re.search(r"林子晴的資料（成績穩定上升：(\d{1,3}(?:→\d{1,3}){2,3})）", skill)
    if not m:
        issues.append("2-1：找不到 Step4 引用林子晴成績趨勢的文字，SKILL.md 結構可能變了")
    else:
        cited = [int(x) for x in m.group(1).split("→")]
        if cited != oct_scores["S001"]:
            issues.append(
                f"2-1 Step4 引用林子晴成績趨勢 {cited}，與 exam-scores-oct.csv 的 {oct_scores['S001']} 不一致"
            )

    for row in watchlist:
        sid = row["學號"]
        seq = num_seq(row["狀況摘要"])
        if seq is None:
            issues.append(f"2-1：priority-watchlist.csv {sid} 的狀況摘要找不到趨勢數字")
            continue
        if sid not in oct_scores:
            issues.append(f"2-1：priority-watchlist.csv 出現 exam-scores-oct.csv 沒有的學號 {sid}")
            continue
        if seq != oct_scores[sid][:3]:
            issues.append(
                f"2-1 priority-watchlist.csv {sid} 狀況摘要寫 {seq}，"
                f"與 exam-scores-oct.csv 前三個月 {oct_scores[sid][:3]} 不一致"
            )
    return issues


# ---------------------------------------------------------------------------
# Lesson 2-3
# ---------------------------------------------------------------------------

def check_2_3():
    issues = []
    base = SKILLS_DIR / "start-2-3"
    skill = read_text(base / "SKILL.md")
    assets = base / "assets/horizon-academy"

    roster = read_csv_rows(assets / "student-roster.csv")
    gender = {r["學號"]: r["性別"] for r in roster}
    attendance = {
        r["學號"]: [r["第一月"], r["第二月"], r["第三月"]]
        for r in read_csv_rows(assets / "attendance.csv")
    }

    male_count = sum(1 for g in gender.values() if g == "男")
    m = re.search(r"男生有\s*(\d+)\s*位", skill)
    if not m:
        issues.append("2-3：找不到「班上男生有 X 位」文字")
    elif int(m.group(1)) != male_count:
        issues.append(f"2-3 Step2 文字寫男生有 {m.group(1)} 位，實際 roster 算出 {male_count} 位")

    def pct(v):
        return int(v.rstrip("%"))

    declining_males = {
        sid for sid, g in gender.items()
        if g == "男" and is_declining([pct(v) for v in attendance[sid]])
    }

    block = extract_between(skill, "**出席率下滑的男生（候選名單）**", "**Say:**")
    table_rows = parse_md_table(block)
    table_ids = {r["學號"] for r in table_rows}

    if declining_males != table_ids:
        issues.append(
            f"2-3 Step3 候選名單與規則不一致：規則算出 {sorted(declining_males)}，"
            f"表格列出 {sorted(table_ids)}"
        )
    else:
        for r in table_rows:
            sid = r["學號"]
            expected = attendance[sid]
            actual = [r["第一月"], r["第二月"], r["第三月"]]
            if actual != expected:
                issues.append(
                    f"2-3 候選名單 {sid} 的百分比 {actual} 與 attendance.csv 的 {expected} 不一致"
                )

    block2 = extract_between(skill, "**吳建宏（S008）本學期摘要**", "**Say:**")
    m2 = re.search(r"出席率：([\d%→]+)", block2)
    if not m2:
        issues.append("2-3：找不到 Step4 吳建宏出席率摘要文字")
    else:
        cited = m2.group(1)
        expected = "→".join(attendance["S008"])
        if cited != expected:
            issues.append(f"2-3 Step4 吳建宏出席率摘要寫 {cited}，與 attendance.csv 的 {expected} 不一致")
    return issues


# ---------------------------------------------------------------------------
# Lesson 3-1
# ---------------------------------------------------------------------------

def check_3_1():
    issues = []
    base = SKILLS_DIR / "start-3-1"
    skill = read_text(base / "SKILL.md")
    assets = base / "assets/horizon-academy"

    csv_scores_map = {
        r["指標"]: [r["第一月"], r["第二月"], r["第三月"]]
        for r in read_csv_rows(assets / "zhang-zhihao-scores.csv")
    }
    block = extract_between(skill, "### Step 2", "### Step 3")
    for r in parse_md_table(block):
        key = r["指標"]
        actual = [r["第一月"], r["第二月"], r["第三月"]]
        expected = csv_scores_map.get(key)
        if expected is None:
            issues.append(f"3-1 Step2 表格出現 zhang-zhihao-scores.csv 沒有的指標「{key}」")
        elif actual != expected:
            issues.append(f"3-1 Step2「{key}」表格寫 {actual}，CSV 是 {expected}")

    csv_hw_map = {
        r["月份"]: r["平均繳交時間"] for r in read_csv_rows(assets / "zhang-zhihao-homework.csv")
    }
    block3 = extract_between(skill, "### Step 3", "### Step 4")
    for r in parse_md_table(block3):
        key = r["月份"]
        expected = csv_hw_map.get(key)
        if expected != r["平均繳交時間"]:
            issues.append(f"3-1 Step3「{key}」表格寫「{r['平均繳交時間']}」，CSV 是「{expected}」")

    obs_text = read_text(assets / "zhang-zhihao-observations.md")
    obs_map = {r["時間"]: r["觀察"] for r in parse_md_table(obs_text)}
    block4 = extract_between(skill, "### Step 4", "### Step 5")
    for r in parse_md_table(block4):
        key = r["時間"]
        expected = obs_map.get(key)
        if expected != r["觀察"]:
            issues.append(f"3-1 Step4「{key}」表格寫「{r['觀察']}」，觀察筆記是「{expected}」")
    return issues


# ---------------------------------------------------------------------------
# Lesson 3-2
# ---------------------------------------------------------------------------

def check_3_2():
    issues = []
    base = SKILLS_DIR / "start-3-2"
    skill = read_text(base / "SKILL.md")
    assets = base / "assets/horizon-academy"

    csv_map = {
        r["評量項目"]: r["平均分"] for r in read_csv_rows(assets / "parent-survey-scores.csv")
    }
    block = extract_between(skill, "**量化評分**", "**Say:**")
    for r in parse_md_table(block):
        key = r["評量項目"]
        expected = csv_map.get(key)
        if expected != r["平均分"]:
            issues.append(f"3-2 Step2「{key}」表格寫 {r['平均分']}，CSV 是 {expected}")

    comments_text = read_text(assets / "parent-survey-comments.md")
    m = re.search(r"（(\d+)\s*份）", comments_text)
    header_total = int(m.group(1)) if m else None

    # The trailing "(其餘 N 份...)" line also starts with "|" and would be
    # mis-parsed as a real data row, so only count rows whose 家長 cell is a
    # single letter (A, B, C...).
    detailed_rows = [
        r for r in parse_md_table(comments_text)
        if re.fullmatch(r"[A-Za-z]", r.get("家長", ""))
    ]
    detailed_count = len(detailed_rows)

    m2 = re.search(r"其餘\s*(\d+)\s*份", comments_text)
    rest_count = int(m2.group(1)) if m2 else None

    if header_total is None or rest_count is None:
        issues.append("3-2：parent-survey-comments.md 找不到總份數或「其餘 X 份」文字")
    elif detailed_count + rest_count != header_total:
        issues.append(
            f"3-2 parent-survey-comments.md 份數對不上：明細 {detailed_count} + "
            f"其餘 {rest_count} != 標題寫的 {header_total}"
        )

    m3 = re.search(r"問卷收回來了，(\d+)\s*份", skill)
    if not m3:
        issues.append("3-2：找不到 Step1「問卷收回來了，X 份」文字")
    elif header_total is not None and int(m3.group(1)) != header_total:
        issues.append(f"3-2 Step1 寫問卷 {m3.group(1)} 份，comments.md 標題寫 {header_total} 份")
    return issues


# ---------------------------------------------------------------------------
# Lesson 3-4
# ---------------------------------------------------------------------------

def check_3_4():
    issues = []
    base = SKILLS_DIR / "start-3-4"
    skill = read_text(base / "SKILL.md")
    assets = base / "assets/horizon-academy"

    reg_rows = read_csv_rows(assets / "trial-class-registrations.csv")
    enrolled_rows = read_csv_rows(assets / "enrolled-students.csv")
    with open(assets / "referral-source-survey.csv", newline="", encoding="utf-8") as f:
        survey_headers = set(next(csv.reader(f)))

    reg_headers = set(reg_rows[0].keys()) if reg_rows else set()
    enrolled_headers = set(enrolled_rows[0].keys()) if enrolled_rows else set()

    if not {"學生姓名", "來源"} <= reg_headers or "狀態" in reg_headers:
        issues.append("3-4 Step2：報名表欄位對照跟 trial-class-registrations.csv 實際欄位對不上")
    if "姓名" in survey_headers or "管道" not in survey_headers:
        issues.append("3-4 Step2：家長問卷欄位對照跟 referral-source-survey.csv 實際欄位對不上")
    if "姓名" not in enrolled_headers or "來源" in enrolled_headers or "管道" in enrolled_headers:
        issues.append("3-4 Step2：入學名單欄位對照跟 enrolled-students.csv 實際欄位對不上")

    # Registrations grouped by source channel.
    reg_by_source = {}
    for r in reg_rows:
        reg_by_source.setdefault(r["來源"], []).append(r["學生姓名"])

    block = extract_between(skill, "**招生通路轉化率分析**", "**Say:**")
    for r in parse_md_table(block):
        source = r["來源管道"]
        if source not in reg_by_source:
            continue  # "待確認" row has no single source, nothing to check
        expected = len(reg_by_source[source])
        actual = int(r["報名人數"])
        if actual != expected:
            issues.append(
                f"3-4 轉化率表格「{source}」報名人數寫 {actual}，registrations.csv 算出 {expected}"
            )

    # Names with an empty 備註 are unambiguous enrollments; names that never
    # appear in enrolled-students.csv at all (clean or marked) never enrolled.
    enrolled_clean = {r["姓名"] for r in enrolled_rows if not r["備註"].strip()}
    enrolled_marked = {r["姓名"] for r in enrolled_rows if r["備註"].strip()}
    reg_names = {r["學生姓名"] for r in reg_rows}
    not_enrolled_at_all = reg_names - enrolled_clean - enrolled_marked

    block2 = extract_between(skill, "**確定對應（已整合）：**", "**需要你確認")
    confirmed_rows = parse_md_table(block2)
    not_enrolled_row = next(
        (r for r in confirmed_rows if r.get("入學狀態") == "未入學"), None
    )
    if not_enrolled_row is None:
        issues.append("3-4：Step3「確定對應」表格找不到「未入學」那一列")
    else:
        table_not_enrolled = {n.strip() for n in not_enrolled_row["姓名"].split("、")}
        if table_not_enrolled != not_enrolled_at_all:
            issues.append(
                f"3-4 未入學名單不一致：規則算出 {sorted(not_enrolled_at_all)}，"
                f"表格寫 {sorted(table_not_enrolled)}"
            )
        table_confirmed_enrolled = set()
        for r in confirmed_rows:
            if r is not not_enrolled_row:
                table_confirmed_enrolled.update(n.strip() for n in r["姓名"].split("、"))
        if table_confirmed_enrolled != enrolled_clean:
            issues.append(
                f"3-4 確定入學名單不一致：規則算出 {sorted(enrolled_clean)}，"
                f"表格寫 {sorted(table_confirmed_enrolled)}"
            )

    block3 = extract_between(skill, "**需要你確認（3 組）：**", "**Say:**")
    missing = sorted(name for name in enrolled_marked if name not in block3)
    if missing:
        issues.append(f"3-4「需要你確認」表格沒有提到（？）標記的入學名單姓名：{missing}")
    if len(enrolled_marked) != 3:
        issues.append(
            f"3-4：enrolled-students.csv 裡（？）標記的人數是 {len(enrolled_marked)}，跟課文說的「3 組」不符"
        )
    return issues


# ---------------------------------------------------------------------------

CHECKS = [
    ("1-1", check_1_1),
    ("2-1", check_2_1),
    ("2-3", check_2_3),
    ("3-1", check_3_1),
    ("3-2", check_3_2),
    ("3-4", check_3_4),
]


def main():
    all_issues = []
    for name, fn in CHECKS:
        try:
            issues = fn()
        except Exception as e:  # noqa: BLE001 - report, don't hide, any parse break
            issues = [
                f"檢查腳本本身出錯：{e!r}"
                "（可能是 SKILL.md 結構被改動，抓不到預期的表格或文字，需要更新 tests/check_lessons.py）"
            ]
        if issues:
            print(f"[FAIL] {name}: {len(issues)} 個不一致")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"[OK] {name}")
        all_issues.extend(issues)

    if all_issues:
        print(f"\n共發現 {len(all_issues)} 個不一致，exit code 非零。")
        return 1
    print("\n全部一致。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
