# 範例資料說明

本文件說明課程練習用的虛擬資料集，所有資料皆為虛構，不包含真實個人資訊。

實際檔案存放在各課的 `.claude/skills/start-X-Y/assets/horizon-academy/` 底下，開課時由該課 SKILL.md 的 Setup 段自動複製到學員工作區的 `horizon-academy/`。完整清單見 `course-structure.json` 的 `assets` 欄。

## 各課資料檔

### 課程 1-1：從原始成績找出需要關注的學生
- `exam-scores.csv`（學號、姓名、月考一、月考二、月考三）：25 位學生的三次月考成績
- `parent-survey.csv`（學號、姓名、滿意度(1-5)、開放填答）：期初家長滿意度問卷

### 課程 2-1：批次產出個人化家長信
- `exam-scores-oct.csv`（學號、姓名、月考一、月考二、月考三、本月測驗）：加上十月測驗成績的月考資料
- `priority-watchlist.csv`（學號、姓名、狀況摘要、處理建議）：延續 1-1 篩選出的優先關注名單

### 課程 2-3：記錯名字也能找到對的人
- `attendance.csv`（學號、姓名、第一月、第二月、第三月）：三個月出席率
- `student-roster.csv`（學號、姓名、性別、家長姓名、聯絡電話）：學生基本資料名單

### 課程 2-5：讓 AI 整理命名混亂的教材資料夾
- `teaching-materials/`：47 份命名混亂的教材檔案（docx／pptx／pdf），練習診斷命名問題與抓出疑似重複檔案

### 課程 3-1：從三個月資料找出張志豪真正的問題
- `zhang-zhihao-scores.csv`（指標、第一月、第二月、第三月）：張志豪三個月的多項指標
- `zhang-zhihao-homework.csv`（月份、平均繳交時間）：張志豪三個月的作業繳交時間趨勢
- `zhang-zhihao-observations.md`：老師對張志豪的考試行為觀察筆記

### 課程 3-2：讓 AI 找出量化和質化之間的矛盾
- `parent-survey-scores.csv`（評量項目、平均分）：學期末家長問卷量化平均分
- `parent-survey-comments.md`：同一份問卷的開放式填答摘錄（28 份）

### 課程 3-3：換受眾，重新包裝同一份資料
- 沿用 3-1 的 `zhang-zhihao-scores.csv`、`zhang-zhihao-homework.csv`、`zhang-zhihao-observations.md`
- `zhang-zhihao-3-1-conclusion.md`：3-1 課程得出的分析結論
- `zhang-zhihao-3-3-parent-update.md`：家長在課程情境中的最新反映

### 課程 3-4：處理三份格式不同的雜亂資料
- `enrolled-students.csv`（姓名、備註）：已報名學生名單
- `referral-source-survey.csv`（管道、人數）：招生管道調查彙總
- `trial-class-registrations.csv`（日期、學生姓名、家長電話、來源）：試聽課報名紀錄

### 課程 4-2：用 AI 整理 200 份命名混亂的教材
- `teaching-materials-200/`：200 份命名混亂的教材檔案（docx／pptx／pdf），批次整理與命名規則練習用

其餘課程（1-2～1-5、2-2、2-4、2-6、3-5、4-1、4-3、4-4）不需要練習資料檔，純對話進行。

## 隱私

這些資料是虛構的，練習時請不要把真實學生個資替換進來。

## 建立你自己的資料

學會課程後，你可以建立符合你學校情境的資料集：

```bash
# 在你的工作目錄建立資料資料夾
mkdir ~/[你的學校名稱]/horizon-academy

# 讓 Claude 幫你生成虛擬資料測試
# 「請幫我生成一份 25 位學生的虛擬名單 CSV，欄位包含：學號、姓名、年級、電話」
```
