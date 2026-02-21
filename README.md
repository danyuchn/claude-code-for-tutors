# Claude Code for Tutors — 教師的 AI 助理實戰課程

> 免費開源課程，專為零程式背景的教師設計。
> 20 堂課 / 5-7 小時 / 節省每週 15 小時行政時間

## 為什麼老師需要 AI 助理？

林欣怡老師有 8 年教齡、120 位學生，熱愛教學——但每週有超過 15 小時花在行政工作上。

| 工作項目 | 現在花的時間 | 學完後 |
|---------|------------|--------|
| 學期末成績彙整 | 4 小時 | 10 分鐘 |
| 每週家長回覆 | 2-3 小時 | 批次生成，各不相同 |
| 社群貼文 | 1 小時/篇 | 有個人風格，不是 AI 味 |

**Claude Code 跟一般 AI 聊天有什麼不同？**
一般 AI 聊天幫你「想」——Claude Code 幫你「做」。它能直接讀取你的 Excel、整理資料夾、批次生成文件，不只是給建議。

不需要寫程式、不需要技術背景，只要會打字就能上手。

## 快速開始

```bash
# 1. 安裝 Claude Code
npm install -g @anthropic-ai/claude-code

# 2. Clone 課程倉庫
git clone https://github.com/danyuchn/claude-code-for-tutors.git
cd claude-code-for-tutors

# 3. 啟動 Claude Code，輸入指令開始第一課
claude
> /start-1-1
```

## 課程目錄

### Module 1：與 AI 說話的藝術（5 課，約 60-80 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 1-1 | 用口語說清楚需求 | [開始學習](modules/module-1-communication/lesson-1-1.md) |
| 1-2 | 給 AI 看，不只是說（截圖/貼文字） | [開始學習](modules/module-1-communication/lesson-1-2.md) |
| 1-3 | 長計畫 vs. 短指令 | [開始學習](modules/module-1-communication/lesson-1-3.md) |
| 1-4 | 主動介入與即時調整 | [開始學習](modules/module-1-communication/lesson-1-4.md) |
| 1-5 | 當 AI 問你問題 | [開始學習](modules/module-1-communication/lesson-1-5.md) |

### Module 2：老師的日常任務（6 課，約 80-100 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 2-1 | 批次生成個人化家長回覆 | [開始學習](modules/module-2-daily-tasks/lesson-2-1.md) |
| 2-2 | 寫出有老師味的社群貼文 | [開始學習](modules/module-2-daily-tasks/lesson-2-2.md) |
| 2-3 | 建立與更新學生資料庫 | [開始學習](modules/module-2-daily-tasks/lesson-2-3.md) |
| 2-4 | 出作業、出考題不再傷腦筋 | [開始學習](modules/module-2-daily-tasks/lesson-2-4.md) |
| 2-5 | 快速整理教學資料 | [開始學習](modules/module-2-daily-tasks/lesson-2-5.md) |
| 2-6 | 搜尋和找回舊資料 | [開始學習](modules/module-2-daily-tasks/lesson-2-6.md) |

### Module 3：數據讓教學更聰明（5 課，約 70-90 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 3-1 | 讀懂學生成績背後的故事 | [開始學習](modules/module-3-data-analysis/lesson-3-1.md) |
| 3-2 | 從家長滿意度調查找改進方向 | [開始學習](modules/module-3-data-analysis/lesson-3-2.md) |
| 3-3 | 追蹤學生進度，一目瞭然 | [開始學習](modules/module-3-data-analysis/lesson-3-3.md) |
| 3-4 | 招生數據分析，讓行銷更精準 | [開始學習](modules/module-3-data-analysis/lesson-3-4.md) |
| 3-5 | 用截圖讓 AI 看懂你的問題 | [開始學習](modules/module-3-data-analysis/lesson-3-5.md) |

### Module 4：自動化你的教學工作流（4 課，約 70-90 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 4-1 | 設計你的第一個教學 Workflow | [開始學習](modules/module-4-automation/lesson-4-1.md) |
| 4-2 | 批量處理：一次搞定 100 件事 | [開始學習](modules/module-4-automation/lesson-4-2.md) |
| 4-3 | 建立學校的知識庫 | [開始學習](modules/module-4-automation/lesson-4-3.md) |
| 4-4 | 你的專屬教學 AI 助理（畢業專案） | [開始學習](modules/module-4-automation/lesson-4-4.md) |

## 授權

本課程的互動式教學框架（slash command 模組結構、`Say:` / `Check:` / `Action:` 教學腳本設計）參考自 [Carl Vellotti](https://x.com/carlvellotti) 的開源課程 [Claude Code for Product Managers](https://github.com/carlvellotti/claude-code-pm-course)（CC BY-NC-ND 4.0）。

本課程所有文字內容、教學情境、虛擬場景（明日學院 Horizon Academy）、角色設定及教材均為原創。

依據原始授權規範，本課程採用 **CC BY-NC-ND 4.0** 授權：
- ✅ 可自由分享（需署名）
- ❌ 不得商業使用
- ❌ 不得修改或製作衍生作品

---

# Claude Code for Tutors — AI Assistant Workshop for Educators

> Free and open-source course designed for teachers with zero programming background.
> 21 lessons / 5-7 hours / Save 15 hours of admin work per week

## About

This course is set in the virtual scenario of **Horizon Academy**, where you play the role of **Teacher Hsin-Yi Lin** — an English teacher with 8 years of experience, learning to use Claude Code from scratch with the guidance of AI coach "Xiao Ai."

No coding skills required. If you can type, you can do this.

## Quick Start

```bash
# 1. Install Claude Code
npm install -g @anthropic-ai/claude-code

# 2. Clone the course repository
git clone https://github.com/danyuchn/claude-code-for-tutors.git
cd claude-code-for-tutors

# 3. Launch Claude Code and start the first lesson
claude
> /start-1-1
```

## Course Outline

| Module | Title | Lessons | Duration |
|--------|-------|---------|----------|
| 1 | The Art of Talking to AI | 5 | ~60-80 min |
| 2 | Daily Teacher Tasks | 6 | ~80-100 min |
| 3 | Data-Driven Teaching | 5 | ~70-90 min |
| 4 | Automate Your Teaching Workflow | 4 | ~70-90 min |

## License

The interactive teaching framework (slash command module structure, `Say:` / `Check:` / `Action:` teaching script pattern) is inspired by [Carl Vellotti](https://x.com/carlvellotti)'s open-source course [Claude Code for Product Managers](https://github.com/carlvellotti/claude-code-pm-course) (CC BY-NC-ND 4.0).

All written content, teaching scenarios, fictional setting (Horizon Academy), character designs, and course materials are original works.

In accordance with the original license, this course is licensed under **CC BY-NC-ND 4.0**:
- ✅ Free to share (with attribution)
- ❌ No commercial use
- ❌ No modifications or derivative works
