# 常態滿額禮合規分析工具

跨品牌通用的滿額禮贈品折扣深度合規分析 Streamlit App。

## 檔案結構

```
gift_compliance_app/
├── app.py              ← 主程式（Streamlit 介面）
├── core.py             ← 核心運算邏輯（不需修改）
├── brand_config.py     ← 品牌欄位對應設定（新增品牌在這裡改）
├── requirements.txt    ← 套件需求
└── README.md
```

## 本機執行

```bash
# 1. 安裝套件
pip install -r requirements.txt

# 2. 啟動
streamlit run app.py
```

瀏覽器自動開啟 http://localhost:8501

## 部署到 Streamlit Cloud（免費，讓所有人能用）

1. 把這個資料夾上傳到 GitHub（建一個 repo）
2. 到 https://streamlit.io/cloud 登入（用 GitHub 帳號）
3. 點「New app」→ 選你的 repo → 選 `app.py`
4. 點「Deploy」→ 等 2 分鐘 → 得到一個網址
5. 把網址分享給各品牌企劃

## 新增品牌

打開 `brand_config.py`，複製 LitoMon 那一組，修改品牌名稱和欄位名稱：

```python
"超凝 Chaogel": {
    "inventory_sheet":  "庫存",
    "realsku_col":      "Real Sku",
    "sku_col":          "Sku",
    "tw_col":           "超凝台灣可用庫存",   # ← 改這個
    "hk_col":           "超凝香港可用庫存",   # ← 改這個
    "exclude_realskus": [],                  # ← 填非品牌商品的 RealSKU
    ...
}
```

存檔後 Streamlit Cloud 自動更新，企劃重新整理頁面就能看到新品牌。

## 需要的四份輸入資料

| 資料 | 格式 | 更新頻率 |
|------|------|---------|
| 庫存表 | .xlsx，需有台灣/香港可用庫存欄 | 每次分析當天下載 |
| 折扣深度規範表 | .xlsx，第一欄為門檻金額 | 規範異動時 |
| 贈品資訊表 | .xlsx，欄位見下方說明 | 每月企劃更新 |
| 門檻設定表 | .xlsx，台灣門檻/港澳門檻兩欄 | 門檻異動時 |

### 贈品資訊表必要欄位

| 欄位名稱 | 說明 |
|---------|------|
| 商品選項貨號 | 和庫存表對應的 key |
| 類型 | `正商品` 或 `特規品` |
| 台幣價格 | 正商品=折扣售價；特規品=成本NTD |
| 港幣價格 | 正商品=HKD售價；特規品=成本HKD |
| 狀態 | `啟用中` / `贈完` / `下架` |
| 是否指定 | `TRUE`/`FALSE`（第一檻指定品免規範檢查）|
| 台灣門檻 | (選填) 目前掛的台灣門檻金額 |
| 港澳門檻 | (選填) 目前掛的港澳門檻金額 |
