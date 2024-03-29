import pickle


class Location:
    def __init__(self,street:str):
        self.street = street

    def __str__(self):
        return f"Location: {self.street}"
    def __repr__(self):
        return f"Location: {self.street}"

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


class Library:
    def __init__(self, title: str,booksNum: int,workers: list,status: bool,location:Location):
        if title:
            self.title = title
        else:
            print("!параметр title должен быть типа string!")
            return
        if booksNum:
            self.booksNum = booksNum
        else:
            print("!параметр booksNum должно быть типа int!")
            return
        if workers:
            for i in range(len(workers)):
                if type(workers[i]) != Worker:
                    print("!параметр workers[] должен быть типа Worker!")
                    return
            self.workers = workers
        else:
            print("!параметр workers должен быть типа list!")
            return
        if status:
            self.status = status
        else:
            print("!параметр status должен быть типа bool!")
            return
        if location:
            self.location = location
        else:
            print("!параметр location должен быть типа Location!")
            return

    def __str__(self):
        return f"Library: {self.title}, {self.booksNum}, {self.workers}, {self.status}, {self.location}"
    def __repr__(self):
        return f"Library: {self.title}, {self.booksNum}, {self.workers}, {self.status}, {self.location}"

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
location = Location('Bondarevka 14b')

l = Library('Miyago',2000,[ane,bob,elena],True,location)

print("'l': ")
# l.showInfo()
print(str(l))
print(l.averageWorkersOld())
print(l.workersJobDay())
print()
print("'new_l': ")
dumpInFile(l)
new_l = loadFromFile()
new_l.showInfo()
print(new_l.averageWorkersOld())
print(new_l.workersJobDay())