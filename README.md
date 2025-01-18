# Facebook Auto-Poke Bot

此專案是一個自動執行 Facebook 戳操作的 Python 腳本，基於 Patchright 和 Playwright 實現。腳本會自動登入 Facebook，並在指定的間隔內執行戳回操作。

---

## 功能
自動登入 Facebook。
自動戳回指定用戶。
可配置的重試次數與等待時間。
支援自動循環執行，直到手動中止。

## 使用 Docker 執行

此專案提供了 Docker 支持，您可以快速啟動並運行腳本，無需手動安裝 Python 或其他依賴。

1. 建立 Docker 映像
確保您在專案目錄下，執行以下指令以建置映像：

``` bash
docker build -t facebook-auto-poke .
```

2. 設定環境變數
在執行容器時，需通過環境變數設定 Facebook 登入帳號、密碼，以及戳操作的目標用戶主頁網址列表 (不需要添加 https://www.facebook.com)：

```
docker run -e EMAIL="your-email@example.com" \
           -e PASSWORD="your-facebook-password" \
           -e MY_LIST="url1,url2" \
           facebook-auto-poke
```

## 配置選項

您可以在程式內修改以下參數以調整行為：

- max_retries：登入失敗的最大重試次數（默認值為 3）。
- wait_time：每次重試前的等待時間（秒）（默認值為 10）。
- interval：每次執行戳操作後的等待間隔（秒）（默認值為 30）。

## 注意事項

此腳本需在合法範圍內使用，請勿執行任何違反 Facebook 使用條款的操作。
使用此腳本可能會因異常活動而觸發 Facebook 的安全檢查。
確保環境變數正確配置，並保護您的敏感信息（例如帳號與密碼）。

## 常見問題

1. 無法登入 Facebook？
	- 檢查 EMAIL 和 PASSWORD 是否正確。
	- 確認 Facebook 是否需要額外的驗證（如雙因素驗證）。
2. 戳操作無法執行？
	- 確保使用的帳號有戳功能，且能正常訪問 https://www.facebook.com/pokes。
	- 確認 MY_LIST 中的 email 是否正確對應到 Facebook 用戶。
	- 確保 Facebook 的語言為中文

## 貢獻

歡迎提交 Issue 或 Pull Request，與我們一起改進此專案！

## 授權

此專案採用 MIT License。

--- 

如果有需要進一步修改，請隨時告訴我！
