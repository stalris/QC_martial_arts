# utils/cli.py  
# This module handles CLI and file selection logic for loading JSON files.
# Can be reused in other scripts

import tkinter as tk
from tkinter.filedialog import askopenfilename
from argparse import ArgumentParser
from pathlib import Path

# constants

VALID_VIDEO_FILES = ('*.mp4', '*.avi', '*.mov', '*.mkv', '*.flv', '*.webm', '*.wmv')

VIDEO_FILETYPES = [
  ('video files', VALID_VIDEO_FILES),
  ('all files', ('*.*'))
]

JSON_FILETYPES = [
  ('json files', ('*.json')),
  ('all files', ('*.*'))
]

# Create the cli parser

# Instantiate an argument parser object
parser = ArgumentParser(description='provide paths or choose via file explorer')

# define expected inputs
parser.add_argument('--json_path', type=Path, help='Path to Alphapose JSON')
parser.add_argument('--video_path', type=Path, help='Path to video file')

# This does the heavy lifting
# Parses the arguments passed in the cli and stored in sys.argv
# arguments are stored in the resulting object
args = parser.parse_args() # args.json_path contains the json path

# Returns a Path object or None
def get_json_path():

  # If user provided a valid path
  if args.json_path and args.json_path.exists():
    return args.json_path
  
  # Otherwise, default to file explorer.
  title='select json file'
  filetypes = JSON_FILETYPES
  path = Path(open_file_explorer(title=title, filetypes=filetypes))
  if path.suffix.lower() not in ('.json'):
    # For now, do nothing except print this and send back no filepath
    print('not a json file')
    path = None
  return path if path else None

def get_video_path():
 
  if args.video_path and args.video_path.exists():
    return args.video_path
  
  title = 'select video file'
  filetypes = VIDEO_FILETYPES
  path = Path(open_file_explorer(title=title, filetypes=filetypes))
  if path.suffix.lower() not in VALID_VIDEO_FILES:
    # For now, do nothing.
    print('unsupported video file, please provide a: ')
    for file in VALID_VIDEO_FILES:
      print(f"\t{file}")
    path = None
  return path if path else None

# Opens the file explorer so the user can select their json file.
def open_file_explorer(title='select file', filetypes=[('all files', '*.*')]):

  # Initialize tkinter and hide root window
  root = tk.Tk()   
  root.withdraw()

  file_path = askopenfilename(
    title=title,
    filetypes=filetypes
  )
  return file_path

# testing logic
def main():
  json_path = get_json_path()
  video_path = get_video_path()

  if json_path:
    print(f'json_path: {json_path}')
  if video_path:
    print(f'video_path: {video_path}')
  if not json_path and not video_path:
    print(f'no file selected')

# Test only when run directly.
if __name__ == '__main__':
  main()
