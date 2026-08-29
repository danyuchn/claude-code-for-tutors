# 貢獻指南

歡迎所有教師、教育工作者和 AI 愛好者貢獻這門課程！

## 你可以貢獻什麼

| 類型 | 說明 | 難易度 |
|------|------|--------|
| 錯誤修正 | 修正課程內容的錯誤或不清楚的地方 | 簡單 |
| 新課程 | 針對特定科目或情境的新課程 | 中等 |
| 課程翻譯 | 將繁體中文課程翻譯成英文、日文等 | 中等 |
| 使用案例 | 分享你真實使用 Claude Code 的教學故事 | 簡單 |
| 範例資料 | 新增更多練習用的範例學生資料或模板 | 簡單 |

## 如何提交課程

### 新課程格式

請參考現有課程格式（如 `.claude/skills/start-1-1/SKILL.md`），這是「一堂課一個資料夾」的互動式教學骨架，一次提交必須包含：

- **`SKILL.md`**：課程腳本本體，frontmatter 需含 `name`、`description`、`disable-model-invocation: true`、`allowed-tools` 四欄，段落順序固定為 Setup → 課名（H1）→ 角色設定 → 學習目標 → 教學流程（Step 1...N，`Say:` / `Check:` / `Action:` / `Present it like this:`）→ 常見問題處理 → 成功判準 → 收尾。
- **`assets/`**：這堂課要用到的真實資料檔（如 CSV），開課時由 Setup 段的指令複製到學員工作區；純敘事、沒有資料表的課可以沒有 assets 內容，但資料夾仍要存在。
- **`course-structure.json`**：新增一列，含 `id`、`module`、`title`、`command`、`skillPath`、`appendixPath`（沒有拍攝腳本可留空字串）、`estimatedMinutes`、`output`、`assets`。

閱讀版拍攝腳本（`modules/` 底下那種格式）改為選交——如果你也想錄成教學影片，可以額外附上，但不是提交的必要條件。

### PR 提交流程

1. Fork 這個倉庫
2. 建立新分支：`git checkout -b lesson/your-lesson-name`
3. 新增你的課程到 `community/contributed-lessons/`
4. 確保課程使用明日學院背景（或說明你的使用情境）
5. 提交 Pull Request，描述你的課程對哪類教師最有幫助

## 行為準則

- 友善、包容，歡迎各種教育背景的貢獻者
- 以「教師使用者」的角度設計內容
- 不要包含真實學生個資
- 保持內容對零程式背景用戶友善

## 聯絡

有任何問題，請開 Issue 討論！
