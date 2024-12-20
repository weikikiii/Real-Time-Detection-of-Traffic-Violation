1.需要修改的路徑

a. app/config/App.php
Line20 : baseURL(架設的伺服器IP)

b. app/Commands/Websocket.php
Line16 : python_path(python環境執行檔 ex .../python.exe)

c. public/python/car_track_website.py
Line70 : ip(同baseURL)

d. public/python/website.py
Line11 : WEBSOCKET_PORT 可以改成自己想要的PORT

e. app/Views/runs/show_video.php
Line33 : ip(port同public/python/website.py)

f. app/Views/monitors/only_one_screen.php
Line64 : ip(port同public/python/website.py)




2.啟動方法

a. php spark serve --host 0.0.0.0 (開啟server)
b. php spark websocket:start (開啟python程式)

3.網頁登入的帳密
帳號 : a
密碼 : a
