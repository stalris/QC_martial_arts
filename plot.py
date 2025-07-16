import cv2
import json
import numpy as np
import matplotlib.pyplot as plt

from os import listdir

demo_video_directory = 'output_json\\demo_video'
file_base_counter = 0

video_path = 'C:\\Users\\someg\\Videos\\martial_arts\\video.avi'
cap = cv2.VideoCapture(video_path)
width_resolution = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height_resolution = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()

dpi = 100
width = width_resolution / dpi
height = height_resolution / dpi

fig = plt.figure(figsize=(width, height), dpi=dpi)

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

# Just open one file for now
file = f'{demo_video_directory}\\video_{file_base_counter:0>12d}_keypoints.json'
with open(file) as f:
  data_dict = json.load(f)

  # convert the json into a numpy array.

  # An array that will contain numpy arrays representing people.
  people = []
  for person in data_dict['people']:
    # Grab the keypoints, stored as an array.
    # See https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/02_output.md
    # For an explanation on this structure.
    keypoints = person['pose_keypoints_2d']

    # Convert to a numpy array.
    np_keypoints = np.array(keypoints)

    # Reshape the array, so its a bunch of 3-tuples
    # Providing an argument of -1 tells numpy to decide the size of that index based on the
    # length of the original and the rest of the arguments.
    people.append(np_keypoints.reshape(-1, 3))

  # convert the original array into a numpy array.
  people = np.array(people)
  print(people)
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
  # plt.gca().invert_yaxis()
  # plt.xlim(0, width_resolution)
  # plt.ylim(0, height_resolution)
  plt.show()
# Iterate over every file in the given directory.
# for file in listdir(demo_video_directory):
#   print(file)
