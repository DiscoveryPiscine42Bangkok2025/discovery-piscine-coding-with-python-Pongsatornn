import sys
def downcase_it(x):
    return x.lower()

params = sys.argv[1:] 
if len(params) == 0:
    print("none")
else:
    for p in params:
        print(downcase_it(p))
