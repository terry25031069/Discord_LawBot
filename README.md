## 環境配置
* 請向藍白要 .env 檔案，並放在專案資料夾之根目錄

## 版本更迭

### version 2.9.1
* 多了 notification.py，現在每 30 分鐘就會去看一次憲法法庭官網，看有沒有新判決出現，如果有就通知大家
* 寫了一個 main.py，開兩個 threads 去啟動 bot.py 跟 notification.py

### version 2.9
* 將程式放在 Docker image 上
* 將法條機器人程式碼整理進 src, res 兩個資料夾
* 建立憲法判決 fetch 功能，並與 Docker Volume 一併使用

### version 2.8.2
* 更改 ! + 法規名稱之演算法，支援以常見簡稱搜尋不在 lawDict.txt 的法條

### version 2.8.1
* 憲法判決現已支援多年度之查詢

### version 2.8.0
* 加入憲法判決之查詢

### version 2.7.8
* 將釋字也加入不用!的行列
* 支援法條項次之查詢

### version 2.7.7
* 將 !! 指令的權限開給特定身份組與特定使用者
* 移除基礎法條的 ! 前置查詢

### version 2.7.6
* 將 !! 指令下放給特定身份組

### version 2.7.5
* 修正 requests 連線數過高之問題
* 將 lawDict 文件化，並修改查詢函數邏輯
* 修正因釋字585號解釋過長而造成的錯誤

### version 2.7.2
* 修正其他法規的搜尋演算法（尋找 DOM element 是否包含 lebal-fei，故目前演算法暫不支援已廢棄法規

### version 2.7.1
* 解決與 MEE6 的 ! 指令前綴衝突

### version 2.7.0
* 如法條並不在 source code 內部，則自動去網站尋找第一個可以點的法條並搜尋

### version 2.6.0
* 新增管理員指令，輸入!!set [法條]，即可設定預設法條
* 將尋找法條之程式碼函數化
