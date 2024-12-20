import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os
import re
import pandas as pd

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.image_folder = ''
        self.images = []
        self.current_index = 0
        self.data_path = []

        frame = ttk.Frame(root)
        frame.pack(padx=10, pady=10)
        
        right_frame = ttk.Frame(frame)
        right_frame.pack(side='left', padx=10)

    
        # 圖片顯示標籤
        self.image_label = ttk.Label(frame)
        self.image_label.pack(side='left', padx=10, pady=10)
        
               
        # 按鈕來選擇資料夾
        folder_button = ttk.Button(right_frame, text="選擇資料夾", command=self.open_folder)
        folder_button.pack(pady=10)
        
        self.folder_label = ttk.Label(right_frame, text="尚未選擇的資料夾", font=("Arial", 12), foreground="green")
        self.folder_label.pack(pady=5)
        
        # 檔名顯示標籤
        self.filename_label = ttk.Label(right_frame, text="", font=("Arial", 12), foreground="blue")
        self.filename_label.pack(pady=5)
        
        # 計數標籤
        self.counter_label = ttk.Label(right_frame, text="")
        self.counter_label.pack(pady=5)
        
        # 亮暗標記
        self.light_label = ttk.Label(right_frame, text="還沒標記", font=("Arial", 12, "bold"),)
        self.light_label.pack(pady=10)

        # 上一張按鈕
        self.prev_button = ttk.Button(right_frame, text="上一張", command=self.show_prev_image)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        # 下一張按鈕
        self.next_button = ttk.Button(right_frame, text="下一張", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)


        # 鍵盤快捷鍵綁定
        self.root.bind("<Left>", lambda event: self.show_prev_image())
        self.root.bind("<Right>", lambda event: self.show_next_image())
        self.root.bind("a", lambda event: self.show_prev_image())  
        self.root.bind("d", lambda event: self.show_next_image())
        self.root.bind('l', lambda event: self.change_light_label(self.current_index))  

        if self.images:
            self.show_image(0)
        else:
            self.counter_label.config(text="未找到圖片")

    def load_images(self):
        image_files = [file for file in os.listdir(self.image_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
        sorted_files = sorted(image_files, key=lambda x: [int(num) for num in re.findall(r'\d+', x)])

        return [os.path.join(self.image_folder, file) for file in sorted_files]

    def show_image(self, index):
        image = Image.open(self.images[index])
        image_path = self.images[index]
        image = image.resize((672,672))  # 調整圖片大小以適配視窗
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo)
        
        # 更新檔名
        filename = os.path.basename(image_path)
        self.filename_label.config(text=f"{filename}")
        
        #更新標籤
        split_filename = filename[3:-4].split('_')
        car_id = int(split_filename[0])
        frame = int(split_filename[1])
        df = pd.read_csv(self.data_path)
        if not df[(df['car_id'] == car_id) & (df['frame'] == frame)].empty:
            label = df[(df['car_id'] == car_id) & (df['frame'] == frame)].iloc[0]['light']
            if label == 0:
                self.light_label.config(text=f"暗")
            else:
                self.light_label.config(text=f"亮")
        else:
            self.light_label.config(text=f"還沒標記")
        self.update_counter()

    def update_counter(self):
        total = len(self.images)
        current = self.current_index + 1
        self.counter_label.config(text=f"第 {current} 張，共 {total} 張")

    def show_next_image(self):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.show_image(self.current_index)
            # self.change_light_label(2,1,1)

    def show_prev_image(self):
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
            self.show_image(self.current_index)
            
    def open_folder(self):
        # 使用 askdirectory() 顯示資料夾選擇對話框
        folder_path = filedialog.askdirectory(title="選擇資料夾")
        video_name = folder_path.split('/')[-1]
        csv_filename = video_name + '.csv'
        self.data_path = csv_filename
        if not os.path.exists(csv_filename):
            columns = ['car_id', 'frame', 'light']
            df = pd.DataFrame(columns=columns)
            df.to_csv(csv_filename, index=False)

        # 如果選擇了資料夾，顯示選擇的路徑
        if folder_path:
            self.folder_label.config(text=f"選擇的資料夾: {folder_path}")
            # 重新載入圖片
            self.image_folder = folder_path
            self.images = self.load_images()
            if self.images:
                self.show_image(0)
            else:
                self.counter_label.config(text="未找到圖片")
        else:
            self.folder_label.config(text="沒有選擇資料夾")
            
    def change_light_label(self, index):
        image_path = self.images[index]
        filename = os.path.basename(image_path)
        split_filename = filename[3:-4].split('_')
        car_id = int(split_filename[0])
        frame = int(split_filename[1])
        df = pd.read_csv(self.data_path)

        if not df[(df['car_id'] == car_id) & (df['frame'] == frame)].empty:
            label = df[(df['car_id'] == car_id) & (df['frame'] == frame)].iloc[0]['light']
            if label == 0:
                df.loc[(df['car_id'] == car_id) & (df['frame'] == frame), 'light'] = 1
                self.light_label.config(text=f"亮")
            else:
                df.loc[(df['car_id'] == car_id) & (df['frame'] == frame), 'light'] = 0
                self.light_label.config(text=f"暗")
            df.to_csv(self.data_path, index=False)
        else:
            new_data = pd.DataFrame({
                'car_id' : [car_id],
                'frame' : [frame],
                'light' : [1],
            })
            # 將新的資料行新增到 DataFrame
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(self.data_path, index=False)
            self.light_label.config(text=f"亮")
            self.sort_csv()
    def sort_csv(self):
        df = pd.read_csv(self.data_path)
        df = df.sort_values(by=['car_id', 'frame'])
        df.to_csv(self.data_path, index=False)

# 主程式
if __name__ == "__main__":
    root = tk.Tk()
    root.title("label_light_tool")
    viewer = ImageViewer(root)
    root.mainloop()
