import sys
import re

pattern = r'\b(\w)(\w)'

for line in sys.stdin:
    line = line.rstrip()   
    result = re.sub(pattern, r'\2\1', line)
    print(result)