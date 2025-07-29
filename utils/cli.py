# utils/cli.py  
# This module handles CLI and file selection logic for loading JSON files.
# Can be reused in other scripts

import tkinter as tk
from tkinter.filedialog import askopenfilename
from argparse import ArgumentParser
from pathlib import Path
def get_json_path():

  # Instantiate an argument parser object.
  parser = ArgumentParser(description='Provide a JSON path or choose via file explorer.')

  # define expected inputs
  parser.add_argument('--json_path', type=Path, help='Path to Alphapose JSON')

  # This parses the arguments passed in the cli and stored in sys.argv.
  # arguments are stored in the resulting object.
  args = parser.parse_args() # args.json_path contains the file path

  # If user provided a valid path
  if args.json_path is not None and args.json_path.exists():
    return args.json_path
  
  # Otherwise, default to file explorer.
  path = open_file_explorer()
  return Path(path) if path else None
  
# Opens the file explorer so the user can select their json file.
def open_file_explorer():

  # Initialize tkinter and hide root window
  root = tk.Tk()   
  root.withdraw()

  file_path = askopenfilename(
    title='Select the JSON file',
    filetypes=[('JSON files', '*.json'), ('all files', '*.*')]
  )
  return file_path

# Test only when run directly.
if __name__ == '__main__':
  path = get_json_path()
  if path:
    print(f'path: {path}')
  else:
    print(f'no file selected')
