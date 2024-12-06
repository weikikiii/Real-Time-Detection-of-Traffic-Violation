import asyncio
import websockets
import json
import requests

#這個檔案是網頁用，目前先固定輸入檔案
WEBSOCKET_PORT = 6789



async def cc_test(websocket):
    # 保持程式持續執行
    while True:
        #等待前端訊息
        start_signal = await websocket.recv()
        if start_signal != "start":
            print("收到無效的啟動訊號")
            return
        
        # 如果收到訊息是start，執行程式(C，也可以換成違規偵測的程式碼)
        response = requests.post("http://100.78.179.98:8080/save_violation_car", json=start_signal)
        if response.status_code == 200:
                print("資料已成功寫入資料庫")
                print(response.text)
        else:
            print(f"寫入失敗: {response.text}")

        # await c(websocket)
        print('ccc')

async def c(websocket):
    event_data = {
    "event": "ccc"   
    }
    print(websocket)
    await websocket.send(json.dumps(event_data))

async def main():
    #開啟伺服器並保持伺服器運行
    async with websockets.serve(cc_test, "0.0.0.0", 6789):
        print(f"WebSocket Server 正在啟動，監聽埠號 {WEBSOCKET_PORT}")
        await asyncio.Future() 


if __name__ == "__main__":
    asyncio.run(main())




