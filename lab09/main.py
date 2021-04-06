import pickle

class Worker:
    def __init__(self,name,old):
        self.name = name
        self.old = old

    def __str__(self):
        return f"Worker: {self.name},{self.old}"
    def __repr__(self):
        return f"Worker: {self.name},{self.old}"
    def showInfo(self):
        print(self.name+ ', '+self.old+'года')
    def getOld(self):
        return self.old
class Library:
    def __init__(self,title,booksNum,workers,status):
        if type(title) == bool:
            print("!Название не может быть bool!")
            return
        else:
            self.title = title
        if type(booksNum) != int:
            print("!Количество книг должно быть типа int!")
            return
        else:
            self.booksNum = booksNum
        if type(workers) != list:
            print("!Параметр workers должен быть типа list!")
            return
        else:
            for i in range(len(workers)):
                if type(workers[i]) != Worker:
                    print("!Все работики должны быть типа Worker!")
                    return
            self.workers = workers
        if type(status) != bool:
            print("!параметр статус должен быть bool!")
            return
        else:
            self.status = status

    def __str__(self):
        return f"Library: {self.title}, {self.booksNum}, {self.workers}, {self.status}"
    def __repr__(self):
        return f"Library: {self.title}, {self.booksNum}, {self.workers}, {self.status}"

    def showInfo(self):
        workersNum = len(self.workers)
        if self.status == True:
            text = 'активна'
        else:
            text = 'не активна'
        print(f"Библиотека {self.title} хранит в себе {self.booksNum} книг. На данный момент имеет статус {text} и насчитывает персонал из {str(workersNum)} человек.")

    def averageWorkersOld(self):
        workersNum = len(self.workers)
        average = 0
        for i in range(workersNum):
            average = average + self.workers[i].old
            i=i+1
        return f"Средний возраст всех работников библиотека равен {average/i}"

    def workersJobDay(self):
        dayInMonth = 31
        workersNum = len(self.workers)
        return f"За месяц каждый работник отработает {int(dayInMonth/workersNum)} смен"

def dumpInFile(obj):
    f = open(r"file.txt",'wb')
    pickle.dump(obj,f)
    f.close()

def loadFromFile():
    f = open(r"file.txt",'rb')
    new_obj = pickle.load(f)
    f.close()
    return new_obj


ane = Worker('Ane',21)
bob = Worker('Bob',40)
elena = Worker('Elena',34)

l = Library('Miyago',2000,[ane,bob,elena],True)

print("'l': ")
l.showInfo()
print(l.averageWorkersOld())
print(l.workersJobDay())
print()
print("'new_l': ")
dumpInFile(l)
new_l = loadFromFile()
new_l.showInfo()
print(new_l.averageWorkersOld())
print(new_l.workersJobDay())