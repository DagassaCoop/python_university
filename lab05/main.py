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
        i=i+1
        numbInStr = newStr.count(simbol)
        if numbInStr == 1:
            print(simbol)
    print('\n'+newStr)


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
    arrVowels = ['а', 'о', 'у', 'е', 'и', 'і'] # массив гласных
    listStr = re.findall('\w+',str)
    N = len(listStr)
    i = 0
    print(listStr)
    # for i in range(N):
    #     simbol = str[i]
    #     j = 0
    #     numConsontants = 0
    #     numVowels = 0
    #     for j in range(len(arrConsonants)):
    #         if simbol == arrConsonants[j]:
    #             numConsontants = numConsontants + 1
    #         j=j+1
    #     j = 0
    #     for j in range(len(arrVowels)):
    #         if simbol == arrVowels[j]:
    #             numVowels = numVowels + 1
    #         j=j+1
    #     i=i+1



# task 1
# task1()

# task 2 (a)
# task2_a()

#task 2 (b)
task2_b()

