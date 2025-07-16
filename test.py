from os import listdir
import json

file_path = 'output_json\\demo_video\\video_000000000000_keypoints.json'

for file in listdir('output_json\\demo_video'):
    print(file)
