import re

dom = re.split('[@.]+', input())
print(dom[1], end='')
