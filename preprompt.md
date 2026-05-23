# Claude Code Pre-Prompt：資料夾與檔案結構規範

請先查看並閱讀：

```bash
/Users/arlen/Desktop/oral_review/prompt.md
```

所有工作都必須在以下目錄下進行：

```bash
/Users/arlen/Desktop/oral_review
```

---

# 1. 建立 reference 資料夾

請在：

```bash
/Users/arlen/Desktop/oral_review
```

底下建立：

```bash
/Users/arlen/Desktop/oral_review/reference
```

之後查閱文獻時，請盡可能完整查閱。  
如果遇到無法查看全文、無法下載、paywall、只能看到 abstract、或其他無法完整閱讀的論文，請在 reference 資料夾中建立：

```bash
/Users/arlen/Desktop/oral_review/reference/reference.md
```

並將無法查看的論文資訊寫入 `reference.md`。

請至少記錄：

- 論文標題
- 作者
- 年份
- 期刊
- DOI 或 PMID（如果有）
- URL（如果有）
- 無法查看的原因

之後我會自行下載這些文獻，再提供給你參考閱讀。

查閱文獻時，請盡可能避開 mega journal、掠奪式期刊，或品質可疑的期刊來源。

---

## 1.1 在 reference.md 中建立文獻總攬表

除了記錄無法查看的文獻外，請在：

```bash
/Users/arlen/Desktop/oral_review/reference/reference.md
```

中建立一個文獻搜尋總結區塊，用來總結目前查閱文獻的進度。

請包含以下內容：

- 總共查到多少篇論文
- 初步篩選後保留多少篇
- 實際可閱讀全文多少篇
- 無法取得全文多少篇
- 建議我還需要補下載多少篇
- 最終建議納入 manuscript 的核心文獻數量
- 各主題分類下目前已有多少篇文獻
- 哪些分類文獻不足，還需要繼續查找

請使用類似以下的總攬表格式：

```markdown
# Reference Summary

## Overall Literature Search Summary

| Category | Count |
|---|---:|
| Total papers identified | |
| Papers excluded after screening | |
| Papers retained for review | |
| Full texts accessible | |
| Full texts inaccessible | |
| Papers user needs to download | |
| Core papers recommended for manuscript | |
| Background/supporting papers | |

## Literature Coverage by Topic

| Topic | Papers identified | Full texts accessible | Full texts inaccessible | Evidence status | Need more papers? |
|---|---:|---:|---:|---|---|
| OSCC/HNSCC cisplatin clinical use | | | | Sufficient / Partial / Insufficient | Yes / No |
| Cisplatin toxicity mechanisms | | | | Sufficient / Partial / Insufficient | Yes / No |
| Circadian molecular nodes | | | | Sufficient / Partial / Insufficient | Yes / No |
| Cisplatin chronotherapy evidence | | | | Sufficient / Partial / Insufficient | Yes / No |
| Circadian monitoring and trial design | | | | Sufficient / Partial / Insufficient | Yes / No |

## Papers Requiring User Download

| Priority | Title | Authors | Year | Journal | DOI/PMID | Reason needed | Relevant section |
|---|---|---|---:|---|---|---|---|
| High / Medium / Low | | | | | | | |

## Notes

- Summarize which areas are already well supported.
- Summarize which areas still lack strong references.
- Identify whether any important evidence comes from low-quality journals and should be avoided or replaced.
- Recommend the next literature-search steps.
```

每次完成一輪文獻搜尋或新增文獻後，請更新這個總攬表。

---

# 2. 建立 figure 資料夾

當開始撰寫論文後，如果有需要圖片或 schematic figure 的地方，請在：

```bash
/Users/arlen/Desktop/oral_review
```

底下建立：

```bash
/Users/arlen/Desktop/oral_review/figure
```

並在其中建立：

```bash
/Users/arlen/Desktop/oral_review/figure/figure.md
```

請在 `figure.md` 中撰寫圖片生成 prompt，讓我可以提供給繪圖 AI 使用。

---

# 3. 建立 full_paper 資料夾

接下來撰寫論文時，請全部使用 LaTeX 格式。

請在：

```bash
/Users/arlen/Desktop/oral_review
```

底下建立：

```bash
/Users/arlen/Desktop/oral_review/full_paper
```

並將論文的 LaTeX 檔案寫在此資料夾中。

---

# 4. 建立 info 資料夾

我會在以下位置建立或放入我自己查閱到的論文與資料：

```bash
/Users/arlen/Desktop/oral_review/info
```

請在後續工作中注意這個資料夾。  
如果其中有我放入的文獻、PDF、筆記或資料，請參考並整合進論文撰寫。

---

# 5. 建立 log 資料夾

請在：

```bash
/Users/arlen/Desktop/oral_review
```

底下建立：

```bash
/Users/arlen/Desktop/oral_review/log
```

請將每個步驟的過程與結果輸出並記錄到 `log` 資料夾中。

log 內容應包含：

- 執行了什麼步驟
- 建立或修改了哪些檔案
- 查閱了哪些文獻或資料
- 遇到哪些無法查看的文獻
- 目前完成狀態
- 下一步建議

---

# 6. 總結

請依照以下資料夾結構進行工作：

```bash
/Users/arlen/Desktop/oral_review/
├── prompt.md
├── reference/
│   └── reference.md
├── figure/
│   └── figure.md
├── full_paper/
│   └── [LaTeX manuscript files]
├── info/
│   └── [user-provided papers and notes]
└── log/
    └── [step-by-step logs]
```
