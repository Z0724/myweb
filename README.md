# 新專案

2023.03.13  

1. 解決卡住的錯誤點，一開始查找錯誤的方向錯了，結果是某個檔案多餘的IMPORT導致互相導入  
2. 成功更深入應用flask-admin，各資料表能繼承做更多細節了，後面再來把各資料表慢慢補上  
  
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
