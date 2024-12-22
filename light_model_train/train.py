from ultralytics import YOLO



model = YOLO('yolov8n.pt')
model.train(data = '/ultralytics/cfg/datasets/car_light_dataset.yaml', epochs=20) //資料路徑, 訓練次數

//yaml檔是yolo所需格式
