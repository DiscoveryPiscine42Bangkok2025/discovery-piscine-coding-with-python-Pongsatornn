import sys
import re
params = sys.argv[1:]
if len(params) != 2:
    print("none")
else:
    x = params[0]
    text = params[1]
    ans = re.findall(x, text)

    if len(ans) == 0:
        print("none")
    else:
        print(len(ans))
