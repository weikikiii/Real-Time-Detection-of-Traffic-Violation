# 專案名稱
即時車輛偵測違規系統
## 簡介
  傳統的車燈違規偵測方式需要警方投入大量人力來監控車輛是否違規，這不僅耗費了大量的時間和人力成本，還容易導致誤判。為了減少警方的人力負擔，並提升交通執法的效率，我們研發一套基於人工智慧的自動化車燈違規偵測系統，取代傳統的人工方式，提高執法的效率及準確率。

## 使用環境
- **作業系統**: Windows
- **開發環境**: 本地開發 (localhost)
- **伺服器環境**: PHP server with Port Forward (端口轉發)
- **程式語言**: 
  - PHP 
  - Python (使用 Anaconda 管理環境)
- **資料庫**: SQLite3 (由 MySQL 切換至 SQLite3)

## 前置準備

1. **安裝所需套件:**
    - python 3.8
    - numpy
    - opencv
    - torch
    - ultralytics

2. **資料庫設置:**
    - 將原有 MySQL 資料庫切換至 SQLite3，並更新 `database.php` 設置。
    - CodeIgniter 4 配置為與 SQLite3 搭配使用。

## 訓練與測試

### 訓練模型
1. 執行訓練指令：
    ```bash
    python train_model.py
    ```
    - 確保訓練資料正確導入，並根據專案需求調整超參數。
    
2. 訓練過程中，記錄模型的訓練與測試指標（準確率、損失值等），保存至 log 文件。

### 測試模型
1. 執行測試指令：
    ```bash
    python test_model.py
    ```
    - 測試集需與訓練集不同，並在測試後輸出結果。

## 功能說明
簡單描述專案的主要功能：
1. **違規檢測系統**: 輸入車輛資訊，檢測車輛是否有違規行為。
2. **結果輸出**: 系統將輸出車輛違規結果及相關數據。

## 文件結構

```bash
|-- my_project/
    |-- app/               # PHP app
    |-- database/          # SQLite3 資料庫
    |-- public/            # 前端文件
        |-- style.css      # 前端樣式
    |-- scripts/           # 訓練與測試的 Python 腳本
        |-- train_model.py
        |-- test_model.py
    |-- README.md          # 專案說明文件