array = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for x in array:
    if x > 5:        
        new.append(x + 2)

new = list(set(new))

print("Original array:", array)
print("New array:", new)
