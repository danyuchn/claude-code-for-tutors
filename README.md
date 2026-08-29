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

每堂課結束後，先輸入 `/clear` 清空對話，再輸入下一堂課的指令。

## 課程目錄

### Module 1：與 AI 說話的藝術（5 課，約 60-80 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 1-1 | 從原始成績找出需要關注的學生 | [開始學習](.claude/skills/start-1-1/SKILL.md) |
| 1-2 | 感覺不對但說不清楚——讓 AI 幫你診斷 | [開始學習](.claude/skills/start-1-2/SKILL.md) |
| 1-3 | 需求太複雜——把條件拆清楚，讓 AI 分別處理 | [開始學習](.claude/skills/start-1-3/SKILL.md) |
| 1-4 | AI 中途停頓——主動介入與即時調整 | [開始學習](.claude/skills/start-1-4/SKILL.md) |
| 1-5 | AI 碰不到你的資料——找到能力邊界，換路前行 | [開始學習](.claude/skills/start-1-5/SKILL.md) |

### Module 2：老師的日常任務（6 課，約 80-100 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 2-1 | 批次產出個人化家長信 | [開始學習](.claude/skills/start-2-1/SKILL.md) |
| 2-2 | 去 AI 化，讓文字有人味 | [開始學習](.claude/skills/start-2-2/SKILL.md) |
| 2-3 | 記錯名字也能找到對的人 | [開始學習](.claude/skills/start-2-3/SKILL.md) |
| 2-4 | 讓 AI 診斷問題，再設計針對性練習題 | [開始學習](.claude/skills/start-2-4/SKILL.md) |
| 2-5 | 讓 AI 整理命名混亂的教材資料夾 | [開始學習](.claude/skills/start-2-5/SKILL.md) |
| 2-6 | 把模糊記憶變成系統化搜尋策略 | [開始學習](.claude/skills/start-2-6/SKILL.md) |

### Module 3：數據讓教學更聰明（5 課，約 70-90 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 3-1 | 從三個月資料找出張志豪真正的問題 | [開始學習](.claude/skills/start-3-1/SKILL.md) |
| 3-2 | 讓 AI 找出量化和質化之間的矛盾 | [開始學習](.claude/skills/start-3-2/SKILL.md) |
| 3-3 | 換受眾，重新包裝同一份資料 | [開始學習](.claude/skills/start-3-3/SKILL.md) |
| 3-4 | 處理三份格式不同的雜亂資料 | [開始學習](.claude/skills/start-3-4/SKILL.md) |
| 3-5 | 從模糊的「感覺不對」診斷公式問題 | [開始學習](.claude/skills/start-3-5/SKILL.md) |

### Module 4：自動化你的教學工作流（4 課，約 70-90 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 4-1 | 把月報流程變成一個可重複用的指令 | [開始學習](.claude/skills/start-4-1/SKILL.md) |
| 4-2 | 用 AI 整理 200 份命名混亂的教材 | [開始學習](.claude/skills/start-4-2/SKILL.md) |
| 4-3 | 把你的經驗整理成 FAQ 知識庫指令 | [開始學習](.claude/skills/start-4-3/SKILL.md) |
| 4-4 | 建立你的個人 AI 協作系統 | [開始學習](.claude/skills/start-4-4/SKILL.md) |

## 可用指令

| 指令 | 功能 |
|------|------|
| `/start-1-1` ~ `/start-1-5` | Module 1 各課 |
| `/start-2-1` ~ `/start-2-6` | Module 2 各課 |
| `/start-3-1` ~ `/start-3-5` | Module 3 各課 |
| `/start-4-1` ~ `/start-4-4` | Module 4 各課 |
| `/hint` | 給提示（不給完整答案） |
| `/recap` | 複習本課重點 |

## 延伸閱讀：影片拍攝腳本

`modules/` 底下保留了這門課早期版本的拍攝腳本（閱讀版），是設計來拍攝教學影片用的文字稿，情境設定與互動版課程大致相同，但部分課程的主題已經和目前的互動版（上方課程目錄）不完全一致，僅供拍片或延伸閱讀參考：

- [Module 1：與 AI 說話的藝術](modules/module-1-communication/)
- [Module 2：老師的日常任務](modules/module-2-daily-tasks/)
- [Module 3：數據讓教學更聰明](modules/module-3-data-analysis/)
- [Module 4：自動化你的教學工作流](modules/module-4-automation/)

## 授權

本課程的互動式教學框架（slash command 模組結構、`Say:` / `Check:` / `Action:` 教學腳本設計）參考自 [Carl Vellotti](https://x.com/carlvellotti) 的開源課程 [Claude Code for Product Managers](https://github.com/carlvellotti/claude-code-pm-course)（CC BY-NC-ND 4.0）。

本課程所有文字內容、教學情境、虛擬場景（明日學院 Horizon Academy）、角色設定及教材均為原創。

**原作者授權**：改編前已於 2026-02-22 透過 X 私訊向 Carl Vellotti 說明本課程的構想（K-12 教師版、繁體中文、免費開源、完整署名），並取得他的明確同意（「Go for it!」）。感謝 Carl 的開放與慷慨。

- Carl 的 X：[@carlvellotti](https://x.com/carlvellotti)
- 原版課程網站：[ccforpms.com](https://ccforpms.com)
- 原版課程倉庫：[carlvellotti/claude-code-pm-course](https://github.com/carlvellotti/claude-code-pm-course)
- Carl 的免費課程總站：[fullstackpm.com](https://fullstackpm.com)

依據原始授權規範，本課程採用 **CC BY-NC-ND 4.0** 授權：
- 可以：自由分享（需署名）
- 不可以：商業使用
- 不可以：修改或製作衍生作品

---

# Claude Code for Tutors — AI Assistant Workshop for Educators

> Free and open-source course designed for teachers with zero programming background.
> 20 lessons / 5-7 hours / Save 15 hours of admin work per week

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

After each lesson, run `/clear` to reset the conversation before starting the next one.

## Course Outline

| Module | Title | Lessons | Duration |
|--------|-------|---------|----------|
| 1 | The Art of Talking to AI | 5 | ~60-80 min |
| 2 | Daily Teacher Tasks | 6 | ~80-100 min |
| 3 | Data-Driven Teaching | 5 | ~70-90 min |
| 4 | Automate Your Teaching Workflow | 4 | ~70-90 min |

## Appendix: Video Shooting Scripts

The `modules/` folder keeps this course's earlier shooting scripts (a reading-only version written for recording instructional videos). The scenario setup mostly matches the interactive lessons above, but some lessons' topics have since diverged from the current interactive version — kept here for reference and video production only:

- [Module 1: The Art of Talking to AI](modules/module-1-communication/)
- [Module 2: Daily Teacher Tasks](modules/module-2-daily-tasks/)
- [Module 3: Data-Driven Teaching](modules/module-3-data-analysis/)
- [Module 4: Automate Your Teaching Workflow](modules/module-4-automation/)

## License

The interactive teaching framework (slash command module structure, `Say:` / `Check:` / `Action:` teaching script pattern) is inspired by [Carl Vellotti](https://x.com/carlvellotti)'s open-source course [Claude Code for Product Managers](https://github.com/carlvellotti/claude-code-pm-course) (CC BY-NC-ND 4.0).

All written content, teaching scenarios, fictional setting (Horizon Academy), character designs, and course materials are original works.

**Permission from the original author**: before adapting the framework, we described this project to Carl Vellotti (a K-12 teacher edition in Traditional Chinese, free, open-source, fully attributed) via X direct message on 2026-02-22 and received his explicit go-ahead ("Go for it!"). Thank you, Carl, for being open and generous with your work.

- Carl on X: [@carlvellotti](https://x.com/carlvellotti)
- Original course site: [ccforpms.com](https://ccforpms.com)
- Original course repository: [carlvellotti/claude-code-pm-course](https://github.com/carlvellotti/claude-code-pm-course)
- Carl's free course library: [fullstackpm.com](https://fullstackpm.com)

In accordance with the original license, this course is licensed under **CC BY-NC-ND 4.0**:
- Allowed: free to share (with attribution)
- Not allowed: commercial use
- Not allowed: modifications or derivative works
