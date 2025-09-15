import sys
params = sys.argv[1:]
if len(params) == 0:
    print("none")
else:
    for p in params:
        if not p.endswith("ism"):
            print(p + "ism")
