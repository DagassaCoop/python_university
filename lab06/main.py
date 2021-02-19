def quackSort(arr):
    """Фунція для швидкого сортування.


    Аргументи:
    arr (list): Массив чисел.


    Результат:
    new_arr (list): Відсортований масив чисел.

    """
    N = len(arr)
    new_arr = []
    i = 0
    for i in range(N):
        new_arr.append(arr[i])
        # new_arr[i]=arr[i]
        i=i+1
    new_arr.sort()
    return new_arr

def valueSearch(arr,value):
    """Функція для пошуку індекса числа.


    Аргументи:
    arr (list): Масив чисел.
    value (int): Число індекс якого потрібно знайти.


    Результат:
    i (int): Індекс числа, яке було задано.
    "Value not find" (str): Результат, якщо такого числа немає в масиві.

    """
    i = 0
    N = len(arr)
    for i in range(N):
        if value == arr[i]:
            return i
        i=i+1
    return "Value not find"

def findMinN(arr,num):
    """Функція для мошуку найменших значень.


    Аргументи:
    arr (list): Масив чисел.
    num (int): Кількість найменших чисел.


    Результа:
    finish_arr (list): Масив, що містить найменші числа.

    """
    new_arr = quackSort(arr)
    finish_arr = []
    i = 0
    for i in range(num):
        finish_arr.append(new_arr[i])
        i=i+1
    return finish_arr

def findMaxN(arr,num):
    """Функція для пошуку найбільших чисел.


    Аргументи:
    arr (list): Масив чисел.
    num (int): Кількість найменших чисел.


    Результат:
    finish_arr (list): Масив, що містить найбільші числа.

    """
    new_arr = quackSort(arr)
    finish_arr = []
    i = -1
    while i >= -num:
        finish_arr.append(new_arr[i])
        i = i - 1
    return finish_arr

def findAverage(arr):
    """Функція для пошуку середнього арифметичного.


    Аргументи:
    arr (list): Масив чисел.


    Результат:
    result (int): Середнє арифметичне.

    """
    result = 0
    N = len(arr)
    i=0
    for i in range(N):
        result = result + arr[i]
    result = result/i
    return result

def onlyOne(arr):
    """Функція для очищеня масиву від дублюючих значень.


    Аргументи:
    arr (list): Масив чисел.


    Результат:
    new_arr (list): Очищений від дублів масив чисел.

    """
    new_arr = []
    i=0
    N = len(arr)
    for i in range(N):
        if arr.count(arr[i]) == 1:
            new_arr.append(arr[i])
        elif arr.count(arr[i]) > 1:
            if i == arr.index(arr[i]):
                new_arr.append(arr[i])
        i=i+1
    return new_arr

arr = [1,3,2,4,6,3,8,1]
print("Start array:")
print(arr)

new_arr = quackSort(arr) # task 1.1
print('Result "quackSort":')
print(new_arr)

value = valueSearch(arr,3) # task 1.2
print('Result "valueSearch":')
print(value)

new_arr = findMinN(arr,5) # task 1.3
print('Result "findMinN":')
print(new_arr)

new_arr = findMaxN(arr,2) # task 1.4
print('Result "findMaxN":')
print(new_arr)

result = findAverage(arr) # task 1.5
print('Result "findAverage":')
print(result)

new_arr = onlyOne(arr) # task 1.6
print('Result "findAverage":')
print(new_arr)

help(quackSort)
help(valueSearch)
help(findMinN)
help(findMaxN)
help(findAverage)
help(onlyOne)