# 新專案

2023.03.15  

1. 文章內容由TEXT改為使用文章編輯器flask_ckeditor  
2. 首頁右上角實裝文章管理，可編輯文章與刪除文章  
預計做分頁  
3. 預計做文章分類管理，大致同上  
4. 預計做左側顯示文章列表  
  
未來規劃：  
碎碎念-更多  
搜尋功能  
會員留言板  
工具箱-LINEBOT  
規劃會員資料頁內容  
  
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
