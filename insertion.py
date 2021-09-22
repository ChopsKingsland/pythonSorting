# print(isinstance(3, float))

array = [1, 5, 6, 8, 10, 26, 53]
value = 26

split = 0

if isinstance(len(array)/2, float): # if split is decimal, round down
    split = int(len(array)/2)
else:
    split = len(array)/2

print(array[split])