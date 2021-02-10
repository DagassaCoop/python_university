import random
import re

# task 1
print('Start task 1')
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

# task 2
print('\nStart task 2')
print('Enter "N":')
N = int(input())
print('Enter "M":')
M = int(input())
arr = [[0] * M for i in range(N)]
i = 0
min = 0
min_index = 0
while i in range(N):
    j = 0
    while j in range(M):
        arr[i][j] = random.randint(-10,10)
        if arr[i][j] < min:
            min = arr[i][j]
            min_index = i
        j=j+1
    i=i+1
print(min_index)
print(min)
print(arr)
temp = arr[min_index]
arr[min_index] = arr[-1]
arr[-1] = temp
print(arr)

# task 3

str = "mama bobu klizmoy v popu naakormila vmig vodoy"
pattern_word = re.findall(r'\w+',str)
pattern_a = re.findall(r'\w+a+', str) # ['mama', 'nakormila']
N = len(pattern_word)
i = 0
result = str
simbol_none = '' # none


for i in range(N):
    simbol = pattern_word[i][-1] # last simbol
    str1 = pattern_word[i]
    if re.search("a",pattern_word[i]):
        new_word = re.sub('a','o',str1, 1)
        simbol_len = len(re.findall(simbol, new_word))  # simbol numbers
        result = re.sub(str1, new_word, result)
    i=i+1
print("\nTask 3\n"+result)

