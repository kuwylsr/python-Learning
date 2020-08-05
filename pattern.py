
import re

test = '00k'
if re.match(r'00\d',test):
    print('ok')
else:
    print('failed')
