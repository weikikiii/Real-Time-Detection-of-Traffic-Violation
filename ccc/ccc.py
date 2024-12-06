from ultralytics import YOLO
import os
import time
import pandas as pd
import argparse
from car_track import car_track

def parse_save(value):
    try:
        numbers = [int(x) for x in value.split(",")]
        # 檢查列表長度是否為 4
        if len(numbers) != 4:
            raise ValueError("The list must contain exactly 4 numbers.")
        # 檢查每個數字是否在 [0, 1] 範圍內
        if any(n < 0 or n > 1 for n in numbers):
            raise ValueError("Each number must be in the range [0, 1].")
        
        return numbers
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid value for --save: {e}")
    

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument(
    '--name', 
    type=str, 
    default="demo_video", 
    help="Name of the folder containing the video files"
)
parser.add_argument(
    '--save', 
    type=parse_save, 
    default="0,0,0,0", 
    help="A comma-separated list of 4 integers to specify saving options:\n - The 1st number: Save YOLO output video (1: yes, 0: no)\n- The 2nd number: Save vehicle images (1: yes, 0: no)\n- The 3rd number: Save vehicle trajectories(image) and turn model predictions(csv file) (1: yes, 0: no)\n- The 4th number: Save wave graphs (1: yes, 0: no)\nExample: --save 1,0,1,0"
)


args = parser.parse_args()



start_time = time.time()
input_folder = "./" + args.name

#output_folder
output_folder = "./" + args.name + "_result"
video_output_folder = output_folder + '/video_output' #存yolo標記過的影片
turn_info_folder = output_folder + '/turn_info' #存軌跡圖、車輛轉彎方向csv檔案（記錄車輛是直走、右轉還是左轉） 
light_info_folder = output_folder + '/light_info' #存亮暗波型圖
carimg_folder = output_folder + '/carimg' #存224*224的車輛圖片
result_folder = output_folder + '/result' #存違規車的圖片


dataset = []


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if not os.path.exists(video_output_folder):
    os.makedirs(video_output_folder)

if not os.path.exists(turn_info_folder):
    os.makedirs(turn_info_folder)

if not os.path.exists(light_info_folder):
    os.makedirs(light_info_folder)

if not os.path.exists(carimg_folder):
    os.makedirs(carimg_folder)

if not os.path.exists(result_folder):
    os.makedirs(result_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        #合成video_path
        video_path = os.path.join(input_folder, filename)
        car_track(video_path, output_folder, args.save)
        

        
# df = pd.DataFrame(dataset, columns=['video_name', 'car_id', 'predict_turn'])
# df = df.sort_values(by=['video_name', 'car_id'], ascending=[True, True])
# df.to_csv(output_folder + '/dataset.csv')


end_time = time.time()
duration_seconds = end_time - start_time

print("Time：", duration_seconds, "秒")  