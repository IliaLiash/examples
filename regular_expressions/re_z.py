import sys
import re

pattern = r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(pattern, line)
    if len(result) >= 1:
        print(line)