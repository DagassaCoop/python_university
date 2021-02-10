import random

# task 1

# print('Enter "N":')
# N = int(input())
# arr = []
# i = 0
# result = 0
#
# while i < N:
#     arr.append(random.randint(-60,60))
#     result = result + arr[i]
#     i = i + 1
#
# print(result)

# task 2

# N = int(input())
# M = int(input())
# arr = [[0] * M for i in range(N)]
# i = 0
# min = 0
# min_index = 0
# while i in range(N):
#     j = 0
#     while j in range(M):
#         arr[i][j] = random.randint(-10,10)
#         if arr[i][j] < min:
#             min = arr[i][j]
#             min_index = i
#         j=j+1
#     i=i+1
# print(min_index)
# print(min)
# print(arr)
# temp = arr[min_index]
# arr[min_index] = arr[-1]
# arr[-1] = temp
# print(arr)

# task 3
import re
str = "mama bobu klizmoy v popu nakormila vmig vodoy"
str1 = "mama"
result = re.findall(r'\w+a',str)
print(result)