# Wild Rift Tools

HIS Tools 旗下嘅 Wild Rift 遊戲助手工具，提供 Champion Pool 管理、戰績記錄同 Battle Assistant 對戰分析。

## 功能

### 1. My Pool Champions
- 從飛書多維表格讀取 Champion 數據
- 按熟練度分組（S+ > S > A > B > Owned）
- 圖庫形式展示，用 Champion Profile Picture
- 按下去查看該 Champion 嘅所有 Fight Records

### 2. Fight Records
- 顯示所有戰績詳情（KDA、Grade、Season、對手、金錢、傷害等）
- 可按 Fight Date、Season、Fight Grade、Kills 排序
- 排序可切換升序/降序

### 3. Battle Assistant
- 選擇我用緊嘅 Champion 同對手 Champion
- 顯示 Matchup 對戰類型（Favorable / Unfavorable / Skill / Hard Counter）
- Matchup Guide：Summary、How to Play、Lane Impact、Why
- 對戰對手歷史戰績統計（場數 / S / A）
- 自己最新 5 場戰績

## 數據來源

- **Champions**：飛書多維表格 `Wild Rift Base` - Champions 表（61 個擁有）
- **Fights**：飛書多維表格 - Fights 表（151 條戰績）
- **Matchups**：飛書多維表格 - Matchups 表（2842 條對局數據）
- **Matchup Guide 來源**：wildriftcore.com

## 文件結構

```
wild-rift-tools/
├── index.html              # 主頁面
├── champions.json          # Champion 數據
├── fights.json             # 戰績數據
├── matchups.json           # Matchup 數據
├── champion-images/        # Champion Profile Pictures（61張）
└── README.md
```

## JSON 結構

### champions.json
```json
[
  {
    "name": "Garen",
    "myPool": "A",
    "role": "Top",
    "tier": null,
    "winRate": 0.5,
    "image": "champion-images/Garen.webp"
  }
]
```

### fights.json
```json
[
  {
    "champion": "Garen",
    "grade": "S",
    "kills": 10,
    "deaths": 2,
    "assists": 5,
    "season": 7,
    "fightDate": "2026-10-10T00:00:00+08:00",
    "opponentChampion": "Darius",
    "line": "Top"
  }
]
```

### matchups.json
```json
[
  {
    "championA": "Garen",
    "championB": "Darius",
    "matchupType": "Unfavorable",
    "edge": -1,
    "lane": "Top",
    "summary": "...",
    "howToPlay": "...",
    "laneImpact": "...",
    "why": "...",
    "source": "https://wildriftcore.com/..."
  }
]
```

## 版本記錄

### v1.01 (2026-10-10)
- 修復 Fight Records 中 KDA 居中對齊問題
- 補全 143 張 Champion Profile Picture（包括對手 Champion）
- 修復 HIS Tools Main Page 工具連接（deployedPage 字段）

### v1.00 (2026-10-10)
- 初始版本
- My Pool Champions 圖庫展示
- Fight Records 詳細查看同排序
- Battle Assistant 對戰分析
- 2842 條 Matchups 數據（含 Summary / How to Play / Lane Impact / Why）

## HIS Tools 系統

本工具屬於 HIS Tools 系統一部分，由 J01C 工作流程管理：
- 數據從飛書多維表格同步
- Prototype 先喺 OneDrive 本地測試
- 用戶確認 OK 後上傳 GitHub
- 自動備份到飛書雲端

---

Wild Rift Tools © 2026.1.01
