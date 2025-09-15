import sys
x = sys.argv[1:]
if len(x) != 2:
    print("none")
else:
    start = int(x[0])
    end = int(x[1])
    ans = list(range(start, end + 1))
    print(ans)
