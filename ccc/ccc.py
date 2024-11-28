from ultralytics import YOLO
import os
import time
import pandas as pd
import argparse
from car_track import car_track

parser = argparse.ArgumentParser()

parser.add_argument('--name', type = str, default="")
args = parser.parse_args()

args.name = "demo_video"
    

start_time = time.time()
input_folder = "./" + args.name

#output_folder
output_folder = "./" + args.name + "_result"
video_output_folder = output_folder + '/videoOutput'
turn_info_folder = output_folder + '/turn_info'
light_info_folder = output_folder + '/light_info'
carimg_folder = output_folder + '/carimg'
result_folder = output_folder + '/result'


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

        car_track(video_path, output_folder)
        

        
# df = pd.DataFrame(dataset, columns=['video_name', 'car_id', 'predict_turn'])
# df = df.sort_values(by=['video_name', 'car_id'], ascending=[True, True])
# df.to_csv(output_folder + '/dataset.csv')


end_time = time.time()
duration_seconds = end_time - start_time

print("Time：", duration_seconds, "秒")  