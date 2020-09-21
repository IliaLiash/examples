import os
import os.path
import shutil

print(os.listdir())
print(os.getcwd())
print(os.listdir('main'))
print(os.path.exists('files.py'))
print(os.path.abspath('files.py'))
print(os.walk('.'))
