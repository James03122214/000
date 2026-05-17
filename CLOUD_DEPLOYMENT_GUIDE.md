# 🌐 台股處置股預警系統 - 雲端部署指南

## 🎯 部署目標
將您的 Streamlit 應用程式部署到雲端，讓使用者可以直接透過網址訪問，無需安裝任何軟體。

## 📋 部署選案對比

| 選案 | 價格 | 難度 | 優點 | 缺點 | 推薦度 |
|------|------|------|------|------|--------|
| **Streamlit Cloud** | 免費 | ⭐ 簡單 | 專為 Streamlit 設計，一鍵部署 | 免費版有限制 | ⭐⭐⭐⭐⭐ |
| **Heroku** | 免費/$5+ | ⭐⭐ 中等 | 成熟穩定，支援多種語言 | 需要設定 Procfile | ⭐⭐⭐⭐ |
| **Railway.app** | 免費/$5+ | ⭐⭐ 簡單 | 現代化介面，自動部署 | 免費版有睡眠模式 | ⭐⭐⭐⭐ |
| **Render.com** | 免費/$7+ | ⭐⭐ 簡單 | 支援自動部署，SSL 免費 | 免費版有冷啟動 | ⭐⭐⭐⭐ |
| **AWS/GCP/Azure** | 付費 | ⭐⭐⭐⭐ 複雜 | 功能強大，可擴展 | 設定複雜，成本高 | ⭐⭐ |

## 🚀 推薦方案：Streamlit Cloud

### 為什麼選擇 Streamlit Cloud？
- ✅ **完全免費** - 每月 750 小時運行時間
- ✅ **一鍵部署** - 從 GitHub 直接部署
- ✅ **自動更新** - 程式碼更新後自動重新部署
- ✅ **SSL 憑證** - 自動提供 HTTPS
- ✅ **專為 Streamlit 設計** - 最佳化支援

---

## 📦 部署前準備

### 1. 準備必要檔案

確保您的專案資料夾包含以下檔案：

```
your-project/
├── app.py                    # 主應用程式
├── requirements.txt          # 套件依賴清單
├── .streamlit/
│   └── config.toml          # Streamlit 配置
└── README.md                # 專案說明
```

### 2. 檢查 requirements.txt

確保您的 `requirements.txt` 包含所有必要套件：

```txt
streamlit>=1.57.0
yfinance>=0.2.18
pandas>=2.0.0
numpy>=1.24.0
```

### 3. 建立 Streamlit 配置

建立 `.streamlit/config.toml` 檔案：

```toml
[theme]
base="light"
primaryColor="#1f77b4"
backgroundColor="#ffffff"
secondaryBackgroundColor="#f0f2f6"
textColor="#262730"
font="sans serif"

[client]
showErrorDetails = true
maxUploadSize = 200

[logger]
level = "info"
```

---

## 🔧 Streamlit Cloud 部署步驟

### 步驟 1: 建立 GitHub 帳號

1. 前往 [github.com](https://github.com) 註冊帳號
2. 建立新的 repository
3. 上傳您的專案檔案

### 步驟 2: 建立 Streamlit Cloud 帳號

1. 前往 [streamlit.io/cloud](https://streamlit.io/cloud)
2. 點擊 "Sign up"
3. 使用 GitHub 帳號登入

### 步驟 3: 部署應用程式

1. 登入後點擊 "New app"
2. 選擇您的 GitHub repository
3. 選擇分支（通常是 `main` 或 `master`）
4. 設定應用程式名稱（如：`stock-alert-system`）
5. 點擊 "Deploy"

### 步驟 4: 等待部署完成

- 部署通常需要 2-5 分鐘
- 您可以看到部署進度
- 完成後會顯示應用程式網址

### 步驟 5: 測試應用程式

- 點擊提供的網址
- 測試股票代碼輸入功能
- 確認所有功能正常運作

---

## 🌐 部署完成後

### 獲得的網址格式
```
https://your-app-name.streamlit.app
```

### 分享給使用者
- 直接分享網址
- 使用者無需安裝任何軟體
- 支援桌面和行動裝置

---

## 🔄 更新應用程式

### 自動更新
1. 在 GitHub 上更新程式碼
2. 推送到 repository
3. Streamlit Cloud 會自動偵測並重新部署

### 手動觸發更新
1. 登入 Streamlit Cloud
2. 找到您的應用程式
3. 點擊 "Re-deploy"

---

## 📊 Streamlit Cloud 限制

### 免費版限制
- **運行時間**: 每月 750 小時
- **記憶體**: 1GB
- **CPU**: 共享資源
- **資料存儲**: 無持久化存儲

### 適用場景
- ✅ 個人專案
- ✅ 小型應用程式
- ✅ 原型開發
- ✅ 教學用途

### 不適用場景
- ❌ 大量使用者
- ❌ 需要資料庫
- ❌ 需要長時間運行
- ❌ 商業級應用程式

---

## 🚀 替代部署方案

### 方案 1: Heroku 部署

#### 優點
- 成熟穩定的平台
- 支援多種語言
- 豐富的附加元件

#### 部署步驟
1. 建立 Heroku 帳號
2. 建立 `Procfile` 檔案
3. 連接 GitHub repository
4. 部署應用程式

#### Procfile 內容
```
web: streamlit run app.py --server.port=$PORT
```

### 方案 2: Railway.app 部署

#### 優點
- 現代化介面
- 自動部署
- 支援多種資料庫

#### 部署步驟
1. 建立 Railway 帳號
2. 從 GitHub 匯入專案
3. 設定環境變數
4. 部署應用程式

### 方案 3: Render.com 部署

#### 優點
- 免費 SSL 憑證
- 自動部署
- 支援 Docker

#### 部署步驟
1. 建立 Render 帳號
2. 連接 GitHub repository
3. 設定構建指令
4. 部署應用程式

---

## 💡 部署最佳實踐

### 1. 程式碼優化
- 減少不必要的計算
- 使用快取機制
- 優化資料載入

### 2. 錯誤處理
- 添加適當的錯誤處理
- 提供友善的錯誤訊息
- 記錄重要錯誤

### 3. 效能監控
- 監控應用程式效能
- 追蹤使用者行為
- 定期檢查日誌

### 4. 安全性
- 不要硬編碼敏感資訊
- 使用環境變數
- 定期更新依賴套件

---

## 🔍 故障排除

### 常見問題

**Q: 部署失敗**
- 檢查 requirements.txt 是否正確
- 確認所有檔案都已上傳
- 查看 Streamlit Cloud 部署日誌

**Q: 應用程式無法啟動**
- 檢查程式碼語法錯誤
- 確認所有套件都已安裝
- 查看錯誤日誌

**Q: 資料抓取失敗**
- 檢查網路連線
- 確認 API 服務正常
- 添加重試機制

**Q: 應用程式運行緩慢**
- 優化程式碼
- 減少不必要的計算
- 使用快取機制

---

## 📞 技術支援

### Streamlit Cloud 支援
- 官方文件: [docs.streamlit.io](https://docs.streamlit.io)
- 社群論壇: [discuss.streamlit.io](https://discuss.streamlit.io)
- GitHub Issues: [github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)

### 其他資源
- Streamlit 教學: [streamlit.io](https://streamlit.io)
- 部署範例: [github.com/streamlit](https://github.com/streamlit)

---

## 🎉 部署完成檢查清單

部署完成後，請確認以下項目：

- [ ] 應用程式可透過網址訪問
- [ ] 股票代碼輸入功能正常
- [ ] 股票資料可正常抓取
- [ ] 預警功能正常運作
- [ ] 股價走勢圖正常顯示
- [ ] 在不同瀏覽器測試
- [ ] 在行動裝置測試
- [ ] 分享網址給他人測試

---

## 🚀 下一步

部署完成後，您可以：

1. **自訂網域** - 購買並設定自訂網域
2. **添加分析** - 整合 Google Analytics
3. **優化 SEO** - 改善搜尋引擎排名
4. **添加認證** - 實現使用者登入功能
5. **擴展功能** - 添加更多股票分析功能

---

**🎉 恭喜！您的台股處置股預警系統現在已經是一個公開網站了！**

*最後更新: 2026年5月*
