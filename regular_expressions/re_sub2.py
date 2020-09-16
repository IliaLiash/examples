import sys
import re

pattern = r'human'

for line in sys.stdin:
    line = line.rstrip()    
    result = re.sub(pattern, 'computer', line)
    print(result)