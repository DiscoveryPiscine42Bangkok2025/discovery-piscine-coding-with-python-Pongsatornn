import sys
if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    result = ""
    for ch in text:
        if ch == "z":   
            result += "z"
    if result == "":
        print("none")
    else:
        print(result)
