# Claude Code for Tutors — 教師的 AI 助理實戰課程

**繁體中文** · [English](#claude-code-for-tutors--ai-assistant-workshop-for-educators)


> 免費開源課程，專為零程式背景的教師設計。
> 主線 24 堂 ＋ 選修 3 堂 / 約 8.8 小時 / 節省每週 15 小時行政時間

本課程的互動式教學框架改編自 [Carl Vellotti](https://x.com/carlvellotti) 的開源課程 [Claude Code for Product Managers](https://github.com/carlvellotti/claude-code-pm-course)，經原作者同意。哪些沿用自原版、哪些是本課程原創，逐項列在[授權](#授權)。

課程作者：Dustin Yuchen Teng（[Dustin's AI Lab](https://agentcrew.cc/blog)）

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

**桌面版（推薦，不需要懂技術）**

1. 到 [GitHub 頁面](https://github.com/danyuchn/claude-code-for-tutors)按綠色「Code」→「Download ZIP」，解壓縮到「文件」資料夾（不需要 git）
2. 打開 Claude 桌面版，上方切到「Code」分頁，選剛解壓縮的資料夾
3. 在對話框打「開始第一課」

如果它沒有開始上課，把這句話貼給它：「請讀 `.claude/skills/start-1-1/SKILL.md`，照裡面的腳本一步一步教我，不要跳步。」

需要 Claude Pro 以上的付費方案。

上完一堂，開一個新對話再說「開始下一課」。

進階的終端機安裝方式見下方「進階：終端機版」。

## 進階：終端機版

```bash
# 1. 安裝 Claude Code（Mac）
curl -fsSL https://claude.ai/install.sh | bash

# Windows（PowerShell）
irm https://claude.ai/install.ps1 | iex

# 2. Clone 課程倉庫
git clone https://github.com/danyuchn/claude-code-for-tutors.git
cd claude-code-for-tutors

# 3. 啟動 Claude Code，輸入指令開始第一課
claude
> /start-1-1
```

每堂課結束後，先 `/clear` 再輸入下一堂課的指令。

## 課程目錄

### Module 1：與 AI 說話的藝術（5 課，約 76 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 1-1 | 從原始成績找出需要關注的學生 | [開始學習](.claude/skills/start-1-1/SKILL.md) |
| 1-2 | 感覺不對但說不清楚——讓 AI 幫你診斷 | [開始學習](.claude/skills/start-1-2/SKILL.md) |
| 1-3 | 需求太複雜——把條件拆清楚，讓 AI 分別處理 | [開始學習](.claude/skills/start-1-3/SKILL.md) |
| 1-4 | AI 中途停頓——主動介入與即時調整 | [開始學習](.claude/skills/start-1-4/SKILL.md) |
| 1-5 | AI 碰不到你的資料——找到能力邊界，換路前行 | [開始學習](.claude/skills/start-1-5/SKILL.md) |

### Module 2：老師的日常任務（6 課，約 118 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 2-1 | 批次產出個人化家長信 | [開始學習](.claude/skills/start-2-1/SKILL.md) |
| 2-2 | 去 AI 化，讓文字有人味 | [開始學習](.claude/skills/start-2-2/SKILL.md) |
| 2-3 | 記錯名字也能找到對的人 | [開始學習](.claude/skills/start-2-3/SKILL.md) |
| 2-4 | 讓 AI 診斷問題，再設計針對性練習題 | [開始學習](.claude/skills/start-2-4/SKILL.md) |
| 2-5 | 讓 AI 整理命名混亂的教材資料夾 | [開始學習](.claude/skills/start-2-5/SKILL.md) |
| 2-6 | 把模糊記憶變成系統化搜尋策略 | [開始學習](.claude/skills/start-2-6/SKILL.md) |

### Module 3：數據讓教學更聰明（5 課，約 76 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 3-1 | 從三個月資料找出張志豪真正的問題 | [開始學習](.claude/skills/start-3-1/SKILL.md) |
| 3-2 | 讓 AI 找出量化和質化之間的矛盾 | [開始學習](.claude/skills/start-3-2/SKILL.md) |
| 3-3 | 換受眾，重新包裝同一份資料 | [開始學習](.claude/skills/start-3-3/SKILL.md) |
| 3-4 | 處理三份格式不同的雜亂資料 | [開始學習](.claude/skills/start-3-4/SKILL.md) |
| 3-5 | 從模糊的「感覺不對」診斷公式問題 | [開始學習](.claude/skills/start-3-5/SKILL.md) |

### Module 5：做出看得見的東西（3 課，約 60 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 5-1 | 幫學習單配一張剛剛好的圖 | [開始學習](.claude/skills/start-5-1/SKILL.md) |
| 5-2 | 讓班上的視覺看起來像同一個人做的 | [開始學習](.claude/skills/start-5-2/SKILL.md) |
| 5-3 | 做一個你自己的班級小工具 | [開始學習](.claude/skills/start-5-3/SKILL.md) |

### Module 4：自動化你的教學工作流（5 課，約 126 分鐘）

| 課號 | 課程名稱 | 連結 |
|------|----------|------|
| 4-1 | 把月報流程變成一個可重複用的指令 | [開始學習](.claude/skills/start-4-1/SKILL.md) |
| 4-2 | 用 AI 整理 200 份命名混亂的教材 | [開始學習](.claude/skills/start-4-2/SKILL.md) |
| 4-3 | 把你的經驗整理成 FAQ 知識庫指令 | [開始學習](.claude/skills/start-4-3/SKILL.md) |
| 4-4 | 建立你的個人 AI 協作系統 | [開始學習](.claude/skills/start-4-4/SKILL.md) |
| 4-5 | 帶著它去動真實的資料 | [開始學習](.claude/skills/start-4-5/SKILL.md) |

### 選修課（3 課，約 75 分鐘）

補齊原版有、主線刻意不教的三項能力。**都不在主線順序裡，上不上都不影響主線的完整性**——因為它們各自有主線承諾之外的門檻，所以獨立出來讓你自己決定。上完之後接你原本的進度往下走，不用重上。

| 課號 | 課程名稱 | 前置 | 你要先知道的門檻 | 連結 |
|------|----------|------|----------------|------|
| 5-4 | 真的把圖生出來 | 5-1 | Google 的生圖模型**沒有免費額度**，要先開通付費才能用 | [開始學習](.claude/skills/start-5-4/SKILL.md) |
| 4-6 | 改壞了能回頭：把你的東西存進 GitHub | 4-2 | 需要註冊 GitHub 帳號（免費），電腦上要有 `git` 與 `gh`（GitHub CLI） | [開始學習](.claude/skills/start-4-6/SKILL.md) |
| 4-7 | 把小工具放上網：同事點連結就能開 | 4-6（硬性） | 發布出去的網站**全世界都看得到**，而且這件事花錢也解決不了（要限定觀看者得用企業方案），所以課程會先帶你把學生姓名換成代號 | [開始學習](.claude/skills/start-4-7/SKILL.md) |

## 怎麼開課

| 桌面版 | 終端機 |
|--------|--------|
| 在對話框說「開始第一課」或「上 1-1」；「下一課」也可以 | `/start-1-1`、`/hint`、`/recap` |

## 延伸閱讀：影片拍攝腳本

`modules/` 底下保留了這門課早期版本的拍攝腳本（閱讀版），是設計來拍攝教學影片用的文字稿，情境設定與互動版課程大致相同，但部分課程的主題已經和目前的互動版（上方課程目錄）不完全一致，僅供拍片或延伸閱讀參考：

- [Module 1：與 AI 說話的藝術](modules/module-1-communication/)
- [Module 2：老師的日常任務](modules/module-2-daily-tasks/)
- [Module 3：數據讓教學更聰明](modules/module-3-data-analysis/)
- [Module 4：自動化你的教學工作流](modules/module-4-automation/)

Module 5（做出看得見的東西）是後來新增的，沒有對應的拍攝腳本。

## 授權

本課程的互動式教學框架參考自 [Carl Vellotti](https://x.com/carlvellotti) 的開源課程 [Claude Code for Product Managers](https://github.com/carlvellotti/claude-code-pm-course)（CC BY-NC-ND 4.0）。

**沿用自原版的部分**（完整列出，不只是「參考」）：

- `.claude/skills/<課程 id>/SKILL.md` ＋ `assets/` 的目錄骨架，與一堂課一個 slash command 的組織方式
- 教學腳本標記：`Say:`（逐字輸出）、`Check:`（停下等學員回應）、`Action:`（AI 自己執行）、`Present it like this:`（輸出格式）
- 課程檔的段落骨架：Setup／角色設定／學習目標／教學流程（分 Step）／常見問題處理／成功判準／收尾
- `_shared/teaching-rules.md` 由每一支 SKILL.md 引用的共用規則架構
- 核心交付模型：**學員全程不碰終端機，所有操作由 AI 執行**；以桌面版為主要教學環境
- 「不要說破腳本」這條規則本身（不宣告自己在照腳本走、不外洩教學指引）
- `course-structure.json` 這個課程清單檔的角色與檔名（schema 已重新設計）

**本課程的原創部分**：

- 27 堂課（主線 24 ＋ 選修 3）的全部文字內容、教學情境與對白（與原版無任何文本重複）
- 虛擬場景明日學院（Horizon Academy）、教學助理「小艾」的人格設定、林欣怡老師與 25 位學生的完整設定
- 全部教材資產：成績單、出席紀錄、家長問卷、招生資料等 CSV，以及刻意設計成命名混亂的 200 餘份教材檔
- 中文教學法規則（先比喻後術語、不一次給太多、學員犯錯溫和指出、為零程式基礎者建立信心）
- **課程本身教的協作方法論**：原版 Foundation 是 Claude Code 的功能導覽（Agents、Sub-agents、Project Memory、鍵盤快捷鍵）；本課程改為教「AI 會怎麼失敗、你怎麼救回來」——講不出問題時怎麼診斷、需求太複雜怎麼拆、AI 中途停頓怎麼介入、碰到能力邊界怎麼換路、從模糊記憶怎麼收斂。功能主題上與原版 1.2–1.7、3.x、4.1–4.3 有對應（檔案樹、平行代理、output style、CLAUDE.md 與子代理、plan 模式與 model effort、圖像與小工具）。**原版的三項能力——真的生成圖片、GitHub 版本控制、線上部署——主線 24 堂刻意不教**，因為它們都需要辦帳號、綁信用卡或把內容公開上網，與本課程對零程式背景教師「不裝東西、不辦金鑰」的承諾衝突；**這三項改以三堂選修課補齊**（5-4 生圖、4-6 版本控制、4-7 部署），能力上不比原版少，但要不要上由讀者自己決定。選修課的門檻在各課開頭誠實講明：生圖需付費開通（Google 官方定價頁對生圖模型的免費額度標示為 Not available），部署走 GitHub Pages 且公開 repo 等於全世界看得到，因此課程會先要求把學生姓名換掉再上傳
- `recap` 與 `hint` 兩支獨立 skill（原版只把它列為「學員可以隨口要求的事」，未實作）
- 移除原版與其商業平台的所有綁定（CLI 工具、帳號登入、進度同步、證書發放），改為完全離線可自學

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

[繁體中文](#claude-code-for-tutors--教師的-ai-助理實戰課程) · **English**


> Free and open-source course designed for teachers with zero programming background.
> 24 core lessons + 3 optional / about 8.8 hours / Save 15 hours of admin work per week

The interactive teaching framework is adapted, with the original author's permission, from [Carl Vellotti](https://x.com/carlvellotti)'s open-source course [Claude Code for Product Managers](https://github.com/carlvellotti/claude-code-pm-course). What is carried over and what is original to this course is listed item by item under [License](#license).

Course author: Dustin Yuchen Teng ([Dustin's AI Lab](https://agentcrew.cc/blog))

## About

This course is set in the virtual scenario of **Horizon Academy**, where you play the role of **Teacher Hsin-Yi Lin** — an English teacher with 8 years of experience, learning to use Claude Code from scratch with the guidance of AI coach "Xiao Ai."

No coding skills required. If you can type, you can do this.

## Quick Start

**Desktop app (recommended, no technical skills needed)**

1. On the [GitHub page](https://github.com/danyuchn/claude-code-for-tutors), click the green "Code" button → "Download ZIP", then unzip it into your Documents folder (no git required)
2. Open the Claude desktop app, switch to the "Code" tab at the top, and select the unzipped folder
3. In the chat box, type "start the first lesson"

If it doesn't start teaching, paste this: "Please read `.claude/skills/start-1-1/SKILL.md` and walk me through it step by step, without skipping steps."

Requires a Claude Pro plan or above.

After each lesson, open a new conversation and say "start the next lesson".

For the advanced terminal setup, see "Advanced: Terminal Version" below.

## Advanced: Terminal Version

```bash
# 1. Install Claude Code (Mac)
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex

# 2. Clone the course repository
git clone https://github.com/danyuchn/claude-code-for-tutors.git
cd claude-code-for-tutors

# 3. Launch Claude Code and start the first lesson
claude
> /start-1-1
```

After each lesson, run `/clear` before starting the next one.

## Course Outline

| Module | Title | Lessons | Duration |
|--------|-------|---------|----------|
| 1 | The Art of Talking to AI | 5 | ~76 min |
| 2 | Daily Teacher Tasks | 6 | ~118 min |
| 3 | Data-Driven Teaching | 5 | ~76 min |
| 5 | Making Things You Can See | 3 | ~60 min |
| 4 | Automate Your Teaching Workflow | 5 | ~126 min |
| — | *Optional lessons (outside the main track)* | 3 | ~75 min |

**Optional lessons** cover the three capabilities the original teaches but the main track deliberately leaves out, because each carries a cost the main track promises not to impose. Skipping them costs you nothing in the main track; each one ends by pointing you back to wherever you left off.

| Lesson | Title | Requires | Up-front cost |
|--------|-------|----------|---------------|
| 5-4 | Actually generate the image | 5-1 | Google's image models have **no free tier**; paid billing required |
| 4-6 | Undo a bad change: put your work on GitHub | 4-2 | A free GitHub account, plus `git` and `gh` installed |
| 4-7 | Put your tool online | 4-6 (required) | A published site is **visible to everyone**, and paying does not change that (restricting viewers needs an enterprise plan), so the lesson replaces student names with codes first |

## Appendix: Video Shooting Scripts

The `modules/` folder keeps this course's earlier shooting scripts (a reading-only version written for recording instructional videos). The scenario setup mostly matches the interactive lessons above, but some lessons' topics have since diverged from the current interactive version — kept here for reference and video production only:

- [Module 1: The Art of Talking to AI](modules/module-1-communication/)
- [Module 2: Daily Teacher Tasks](modules/module-2-daily-tasks/)
- [Module 3: Data-Driven Teaching](modules/module-3-data-analysis/)
- [Module 4: Automate Your Teaching Workflow](modules/module-4-automation/)

## License

The interactive teaching framework is adapted from [Carl Vellotti](https://x.com/carlvellotti)'s open-source course [Claude Code for Product Managers](https://github.com/carlvellotti/claude-code-pm-course) (CC BY-NC-ND 4.0).

**Carried over from the original** (listed in full, not just "inspired by"):

- The `.claude/skills/<lesson-id>/SKILL.md` + `assets/` directory layout, and the one-slash-command-per-lesson organisation
- The teaching-script markers: `Say:` (deliver verbatim), `Check:` (stop and wait for the learner), `Action:` (the agent performs it), `Present it like this:` (output format)
- The lesson-file section skeleton: Setup / Your Role / Learning Objectives / Teaching Flow (in Steps) / Common Questions / Success Criteria / Sendoff
- The shared-rules architecture: a `_shared/teaching-rules.md` that every SKILL.md reads first
- The core delivery model: **the learner never touches a terminal; the agent performs every action**, taught primarily in the desktop app
- The "never break character about the script" rule itself
- The role and filename of `course-structure.json` as the course manifest (the schema was redesigned)

**Original to this course**:

- All written content, teaching scenarios, and dialogue across all 27 lessons (24 core + 3 optional; no textual overlap with the original)
- The fictional setting (Horizon Academy), the "Xiao-Ai" teaching-assistant persona, and the full cast of Ms. Lin and 25 students
- Every course asset: exam scores, attendance records, parent surveys, enrolment data, plus 200+ deliberately messy teaching files
- The Chinese-language pedagogy rules (metaphor before jargon, small steps, correct gently, build confidence for non-programmers)
- **The collaboration methodology the course actually teaches**: the original's Foundation is a feature tour of Claude Code (Agents, Sub-agents, Project Memory, keyboard navigation). This course teaches how the AI fails and how you recover — diagnosing a problem you cannot articulate, decomposing tangled requirements, intervening when the agent stalls, recognising a capability boundary and routing around it, converging from a vague memory. Topic-wise it now maps onto the original's 1.2–1.7, 3.x and 4.1–4.3. Three of the original's capabilities — real image generation, GitHub version control, and online deployment — are deliberately **not** in the 24-lesson main track, because each requires an account, a credit card, or publishing content to the open web, which conflicts with this course's no-install, no-API-key promise to teachers with no programming background. **All three are covered instead by three optional lessons** (5-4 image generation, 4-6 version control, 4-7 deployment), so nothing the original teaches is missing — taking them is the reader's choice. Each optional lesson states its cost up front: image generation requires paid billing (Google's own pricing page lists no free tier for the image models), and deployment uses GitHub Pages, where a public repository is visible to everyone, so the lesson replaces real student names before anything is uploaded
- The standalone `recap` and `hint` skills (the original lists these only as things a learner may ask for; they are not implemented)
- Removal of every dependency on the original's commercial platform (its CLI, account login, progress sync, and certificates), making this course fully self-contained and offline-capable

**Permission from the original author**: before adapting the framework, we described this project to Carl Vellotti (a K-12 teacher edition in Traditional Chinese, free, open-source, fully attributed) via X direct message on 2026-02-22 and received his explicit go-ahead ("Go for it!"). Thank you, Carl, for being open and generous with your work.

- Carl on X: [@carlvellotti](https://x.com/carlvellotti)
- Original course site: [ccforpms.com](https://ccforpms.com)
- Original course repository: [carlvellotti/claude-code-pm-course](https://github.com/carlvellotti/claude-code-pm-course)
- Carl's free course library: [fullstackpm.com](https://fullstackpm.com)

In accordance with the original license, this course is licensed under **CC BY-NC-ND 4.0**:
- Allowed: free to share (with attribution)
- Not allowed: commercial use
- Not allowed: modifications or derivative works
