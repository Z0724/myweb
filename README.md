# 新專案

2023.03.23  

1. 開始處理權限功能  
解決資料表儲存欄位的問題，用JSON存列表資料  
MYSQL不支持ARRAY，除了JSON另外可用JOIN字串處理  
  
未來規劃：  
搜尋功能(學習中)  
會員留言板  
工具箱-LINEBOT  
規劃會員資料頁內容  
登入時間  
註冊功能實裝EMAIL驗證  
美化文章顯示頁面  
  
網頁樣式套版(完成)  
串接Mysql，套flask_sqlalchemy建立資料表並操作(完成)  
設置flask_migrate，可更新資料庫並管理更新版本(完成)  
設置.env , .gitignore(完成)  
逐漸將程式碼轉工廠模式(進行中)  
解析開源專案中  
  
寫筆記(技術文章)  
Flask-admin(完成)  
flask_sqlalchemy(尚未)  
其他  
  
紀錄migrate指令  
$ flask db migrate  
$ flask db upgrade  
$ flask db stamp head # Target database is not up to date錯誤時用  
$ flask db heads # 看版本  
