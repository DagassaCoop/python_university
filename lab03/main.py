import random

print('Enter "N":')
N = int(input())
arr = []
i = 0
result = 0

while i < N:
    arr.append(random.randint(-60,60))
    result = result + arr[i]
    i = i + 1

print(result)

