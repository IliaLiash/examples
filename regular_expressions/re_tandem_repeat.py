import sys
import re

pattern = r'\b(\w+)\1\b'

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(pattern, line)
    if len(result) >= 1:
        print(line)