import os

w = open('ans.txt','w')
current_dirs = []

for current_dir, dirs, files in os.walk('main'):
    for element in files:
        if element[-3:] == '.py' and current_dir not in current_dirs:
            current_dirs.append(current_dir)
            w.write(current_dir + '\n')
            
w.close()