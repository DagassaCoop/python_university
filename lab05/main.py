import re



def task1():
    print('Enter first word: ')
    str1 = input()
    print('Enter second word: ')
    str2 = input()
    newStr = str1+str2
    N = len(newStr)
    i = 0
    for i in range(N):
        simbol = newStr[i]
        numbInStr = newStr.count(simbol)
        if numbInStr > 1:
            if i == newStr.find(simbol):
                print(simbol)
        i=i+1

    # print('\n'+newStr)


def task2_a():
    str = "Sed consectetur, risus sit amet porttitor vulputate, libero lectus aliquet magna, ut tincidunt risus libero in ipsum."
    i = 0
    arr1 = []
    arr2 = []
    arr3 = []
    newStr = ''.join(re.findall('\w', str))
    N = len(newStr)
    for i in range(N):
        simbol = newStr[i]
        if newStr.find(simbol) == i:
            arr1.append(simbol)
        if newStr.count(simbol) == 1:
            arr3.append(simbol)
        elif newStr.count(simbol) > 1:
            if newStr.find(simbol) == i:
                arr2.append(simbol)
        i=i+1
    print(arr1)
    print(arr2)
    print(arr3)

def task2_b():
    str = 'МАТИ МОЄЇ ПОДРУГИ ЦІКАВИТЬСЯ ЛИШЕ СПОРТОМ ТА ЦІНАМИ НА НОВІ БУДИНКИ, ДИВНА ЖІНКА'
    arrConsonants = ['в', 'м', 'н', 'л', 'р', 'й', 'б', 'г', 'д', 'ж', 'з', 'п', 'х', 'к', 'т', 'ш', 'с', 'ч', 'ц', 'ф'] # массив согласных
    arrVowels = ['а', 'о', 'у', 'е', 'и', 'і','ї','є'] # массив гласных
    listStr = re.findall('\w+',str)
    N = len(listStr)
    i = 0
    for i in range(N):
        M = len(listStr[i])
        j = 0
        numConsontants = 0
        numVowels = 0
        for j in range(M):
            t = 0
            simbol = listStr[i][j].lower()
            for t in range(len(arrConsonants)):
                if simbol == arrConsonants[t]:
                    numConsontants = numConsontants + 1
                    break
                t=t+1
            t = 0
            for t in range(len(arrVowels)):
                if simbol == arrVowels[t]:
                    numVowels = numVowels + 1
                    break
                t=t+1
            j=j+1
        # print("Количество гласных: ")
        # print(numVowels)
        # print("Количество согласных: ")
        # print(numConsontants)
        if numConsontants > numVowels:
            listStr[i] = listStr[i].lower()
        i=i+1
    print('Дано: ' + str)
    str = ' '.join(listStr)
    print('Результат: ' + str)


# task 1
task1()

# task 2 (a)
task2_a()

#task 2 (b)
task2_b()
