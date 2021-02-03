print('Enter "N":')
N = input()

list = list(N)

i = 1
maxVal = int(list[i-1])
while i != len(list):
    if int(list[i]) > int(list[i-1]):
        maxVal = int(list[i])
    i = i + 1

print(maxVal)
