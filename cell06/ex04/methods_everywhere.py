
import sys
def shrink(i):
    return i[:8]

def enlarge(j):
    return j + "Z" * (8 - len(j))

x = sys.argv[1:]

if len(x) < 1:
    print("none")
else:
    for p in x:
        if len(p) > 8:
            print(shrink(p))
        elif len(p) < 8:
            print(enlarge(p))
        else: 
            print(p)
