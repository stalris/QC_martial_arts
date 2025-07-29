import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
import re 
from os import listdir

direct = input('Enter Json Folder you are using (FOLDER MUST BE IN output_json1):')
demo_video_directory = f'output_json1/{direct}'

# TODO: make this a module
#call clear.py to clear newplots folder after every use
# with open("clear.py") as f:
#   exec(f.read())

video_reference = input('Make sure your video is in the vidoes file and then input the name AND extension!: ')
video_path = f'videos/{video_reference}'

# Iterate over every file in the given directory.
# Finds all the json files that contains keypoints that OpenPose produces as output.
def extract_frame_number(filename):
    match = re.search(r'.*?_(\d+)_keypoints\.json', filename)
    return int(match.group(1)) if match else -1

# Grab the dimensions of the video you're examining.
def getDimensions(video_path):
  capture = cv2.VideoCapture(video_path)
  width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
  capture.release()
  return width,height

# Create a figure in matplotlib with the specified dimensions.
dpi = 100
width, height = getDimensions(video_path)
fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)

# Edges for the keypoints, per the openpose documentation.
edges = [
  (0, 1),
  (1, 2),
  (2, 3),
  (3, 4),
  (1, 5),
  (5, 6),
  (6, 7),
  (1, 8),
  (8, 9),
  (9, 10),
  (10, 11),
  (11, 24),
  (11, 22),
  (22, 23),
  (8, 12),
  (12, 13),
  (13, 14),
  (14, 21),
  (14, 19),
  (19, 20),
  (0, 15),
  (15, 17),
  (0, 16),
  (16, 18)
]


# Get and sort the list of files by frame number
files = sorted(listdir(demo_video_directory), key=extract_frame_number)
ite=0
for cur_file in files: 

  # Open each json file
  json_path= f"{demo_video_directory}/{cur_file}"
  with open(json_path) as f:
    data_dict = json.load(f)

  # convert the json into a numpy array.
  # An array that will contain numpy arrays representing people.
  people = []

  
  for person in data_dict['people']:
    # Grab the keypoints, stored as an array & Convert to a numpy array.
    keypoints = person['pose_keypoints_2d']
    np_keypoints = np.array(keypoints)
    people.append(np_keypoints.reshape(-1, 3))
  # convert the original array into a numpy array.
  people = np.array(people)

  # loop over every person
  for person in people:
  # draw only visible nodes, by checking its confidence value
    for keypoint in person:
      if keypoint[2] != 0:
        plt.plot(keypoint[0], keypoint[1], 'o')
  
    # draw the edges.
    for i, j in edges:
      node1 = person[i]
      node2 = person[j]
      
      if node1[2] != 0 and node2[2] != 0:
        x_coords = [person[i, 0], person[j, 0]]
        y_coords = [person[i, 1], person[j, 1]]
        plt.plot(x_coords, y_coords, color='red')

  plt.gca().invert_yaxis()
  plt.savefig(f"newplots/plot_{ite}.png")  # saves to a folder named 'plots'
  ite=ite+1
  plt.close(fig)
  # plt.show() DONT UNCOMMENT THIS OR THE PROGRAM WILL LOAD 200+ IMAGES SIMULTANEOUSLY 

#call the video.py file to compile into video
with open("video.py") as f:
  exec(f.read())
print("Done!")

# for file in files:
#     print(file)
  # plt.gca().invert_yaxis()
  # plt.xlim(0, width_resolution)
  # plt.ylim(0, height_resolution)
  # plt.gca().invert_yaxis()
  # plt.show()
# Iterate over every file in the given directory.
# for file in listdir(demo_video_directory):
#   print(file)
