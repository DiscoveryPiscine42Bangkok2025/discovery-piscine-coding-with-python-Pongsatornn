import sys
params = sys.argv[1:]
if len(params) == 0:
    print("none")
else:
    print(params[0].upper())

