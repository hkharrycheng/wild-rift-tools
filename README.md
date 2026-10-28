# Wild Rift Tools

HIS Tools 旗下嘅 Wild Rift 遊戲助手工具，提供 Champion Pool 管理、戰績記錄同 Battle Assistant 對戰分析。

## 功能

### 1. My Pool Champions
- 從飛書多維表格讀取 Champion 數據（經 Cloudflare Worker 即時讀取）
- 按熟練度分組（S+ > S > A > B > Owned）
- 圖庫形式展示，用 Champion Profile Picture
- 按下去查看該 Champion 嘅所有 Fight Records

### 2. Fight Records
- 專業電競風格 Dashboard：Summary 面板（S/A Rating、Avg KDA、Gold/Damage/CC/Ward/TFP 條形圖）
- 每場對戰卡片顯示日期橫幅、Grade、KDA、對手、7 項數據統計、截圖縮圖
- 截圖可點擊放大全螢幕 Lightbox 觀看
- 篩選：英雄 / Lane / 對局類型
- 排序：日期 / Kills / Damage / Gold / CC
- 即時 Refresh 按鈕（從 Cloudflare Worker 拉最新飛書數據）

### 3. Champion Leaderboard
- 從 Fights 數據自動計分：S（含 S+）= 2 分，A（含 A+/A-）= 1 分
- 同分按總 Kills 降序排序
- 6 個 Lane 快速過濾按鈕：All / Baron / Jungle / Mid / Dragon / Support
- 排名 Top 1/2/3 顯示 🥇🥈🥉 獎牌 icon
- 點擊 Champion 跳轉到 Fights 頁篩選該英雄

### 4. Battle Assistant
- 選擇 Lane 後顯示可用 Champion dropdown
- 顯示 Matchup 對戰類型（Hard Counter / Soft Counter / Even / Farm）
- Matchup Guide：Summary、How to Play、Lane Impact、Why
- 左側「Record vs Opponent」：最近 5 場，每行左側顯示日期（MM/DD 灰色小字）
- 右側「Recent Record」：最近 10 場，每行左側顯示日期
- 數據源：Cloudflare Worker 即時讀取飛書 Fights / Champions

### 5. News
- 官方新聞 + YouTube 影片統一鏡像（news-cache.json）
- 分類篩選：全部 / 官方 / YouTube

## 數據來源

- **Champions**：飛書多維表格 `Wild Rift Base` - Champions 表
- **Fights**：飛書多維表格 - Fights 表（164 場）
- **Matchups**：飛書多維表格 - Matchups 表（2842 條對局數據）
- **Matchup Guide 來源**：wildriftcore.com
- **Cloudflare Worker**：`https://j07-wr-proxy.hkharrycheng.workers.dev`（代理飛書 API + 截圖 file_token）

## 文件結構

```
wild-rift-tools/
├── index.html              # 主頁面
├── champions.json          # Champion 數據（本地備份）
├── fights.json             # 戰績數據（本地備份）
├── matchups.json           # Matchup 數據
├── news-cache.json         # 新聞鏡像
├── champion-images/        # Champion Profile Pictures
└── README.md
```

## 版本記錄

- **v1.13**（2026-10-28）：刪除殘留的舊版 Fight Records modal overlay；全部 UI 文字改為英文（Battle / Champions / Fights / News）；積分榜 sub-toggle 改為 6 個直接 Lane 按鈕（All/Baron/Jungle/Mid/Dragon/Support）；Top 1/2/3 加 🥇🥈🥉 獎牌 icon；footer 版本 2026.1.06
- **v1.12**（2026-10-27）：Champions 頁新增「🏆 積分榜」模式（S=2分/A=1分計分，同分按 Kills 排序），支援「📊 分Lane排名」和「📋 全部合一」兩種 layout；修復 Fights 頁 Lane filter 選 Top 無結果（數據實際為 Baron）；footer 版本 2026.1.05；commit 7e29559c
- **v1.11**（2026-10-27）：Battle Assistant record-mini 列表左側加日期（MM/DD 灰色小字）；對手戰績擴至 5 場、最新戰績擴至 10 場；footer 版本 2026.1.04；commit 73cd4042
- v1.02 (2026-10-13): header 改用圖標相片 LOGO（移除 ⚔️ emoji）

### v1.01 (2026-10-10)
- 修復 Fight Records 中 KDA 居中對齊問題
- 補全 Champion Profile Picture
- 修復 HIS Tools Main Page 工具連接

### v1.00 (2026-10-10)
- 初始版本
- My Pool Champions 圖庫展示
- Fight Records 詳細查看同排序
- Battle Assistant 對戰分析
- 2842 條 Matchups 數據

## HIS Tools 系統

本工具屬於 HIS Tools 系統一部分，由 J07 工作流程管理：
- 數據從飛書多維表格同步（Cloudflare Worker 即時讀取）
- Prototype 先喺 OneDrive 本地測試
- 用戶確認 OK 後上傳 GitHub
- Cloudflare Pages 自動部署

---

Wild Rift Tools © 2026.1.06
