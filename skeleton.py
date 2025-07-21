import numpy as np
import json
import matplotlib.pyplot as plt

file_path = 'C:\\Users\\theea\\Documents\\school\\QC_martial_arts\\output_json\\demo_video\\video_000000000000_keypoints.json'

with open(file_path, 'r') as file:
    data_dict = json.load(file)
    
    for key in data_dict:
        print(key)
    
    people = []
    for person in data_dict['people']:
        keypoints = person['pose_keypoints_2d']

        np_array = np.array(keypoints)

        np_array = np_array.reshape(-1, 3)
        people.append(np_array)
    people = np.array(people)
    
    print(data_dict['people'])
    print(people)
