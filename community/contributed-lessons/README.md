# 社群貢獻課程

歡迎所有教師貢獻針對不同科目、年齡層或情境的課程！

## 如何貢獻課程

### 貢獻類型

| 類型 | 說明 | 適合誰 |
|------|------|--------|
| 科目專屬課程 | 針對數學、音樂、體育等的 AI 應用 | 各科老師 |
| 年齡層調整 | 幼兒園、高中、成人班的不同操作方式 | 有特定學齡經驗的老師 |
| 語言翻譯 | 英文版、日文版、東南亞語言版 | 多語言使用者 |
| 情境變體 | 線上教學、特教班、國際學校 | 有特殊教學情境的老師 |

### 提交步驟

1. Fork 此倉庫
2. 在 `community/contributed-lessons/` 建立你的課程資料夾
   - 資料夾命名：`[科目]-[主題]-[作者名稱]/`
   - 例：`math-excel-analysis-teacher-chen/`
3. 遵照課程格式（參考 `.claude/skills/start-1-1/SKILL.md`）
4. 提交 Pull Request，說明：
   - 這個課程適合哪類老師
   - 和原版課程有什麼不同
   - 你實際測試過的情境

### 課程格式要求

必須包含：
- `SKILL.md`：frontmatter 四欄（`name`、`description`、`disable-model-invocation: true`、`allowed-tools`）齊全，段落順序固定為 Setup → 課名（H1）→ 角色設定 → 學習目標 → 教學流程（`Say:` / `Check:` / `Action:` / `Present it like this:`）→ 常見問題處理 → 成功判準 → 收尾
- 若有練習用的真實資料檔，放進同一資料夾的 `assets/`
- 在 `course-structure.json` 補一列，含 `id`、`module`、`title`、`command`、`skillPath`、`appendixPath`、`estimatedMinutes`、`output`、`assets`

閱讀版拍攝腳本為選交項目，不是必要條件。

---

## 已貢獻課程

*目前還沒有貢獻課程——你可以成為第一個！*

| 課程名稱 | 作者 | 科目/情境 | 新增日期 |
|----------|------|-----------|----------|
| （待新增）| | | |

---

## 貢獻者名單

感謝所有貢獻者讓這個課程更豐富！

*你的名字會在這裡。*
