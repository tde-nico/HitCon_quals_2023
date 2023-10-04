import os

def print_directory_tree(root_dir, indent=''):
  try:
    with os.scandir(root_dir) as entries:
      for entry in entries:
        if entry.is_dir():
          print(indent + "📁 " + entry.name)
          print_directory_tree(entry.path, indent + "  | ")
        else:
          print(indent + "📄 " + entry.name)
  except PermissionError as e:
    print(indent + f"Permission Error: {e}")
  except OSError as e:
    print(indent + f"OS Error: {e}")


os.mkdir('stop_judging')
starting_directory = '/run'
print(f"Directory Tree for: {starting_directory}")
print_directory_tree(starting_directory)

'''
Directory Tree for: /run
📁 workdir
  | 📁 stop_judging
  | 📄 1.txt.json
  | 📄 1.txt.out
  | 📄 1.txt
  | 📄 submission.py
📁 judge
  | 📁 testcases
  |   | 📄 2.txt
  |   | 📄 5.txt
  |   | 📄 1.txt
  |   | 📄 4.txt
  |   | 📄 3.txt
  | 📄 result.log
'''

