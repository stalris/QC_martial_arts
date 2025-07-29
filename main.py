from utils.cli import get_json_path

# Grabs the json file path if provided as an argument.
# Otherwise, opens the file explorer to select the file.
json_path = get_json_path()
if json_path:
  print(json_path)
else:
  print(f'no file provided')
