import pickle
from abc import ABC, abstractmethod

class Location:
    def __init__(self,street:str):
        self.street = street

    def __str__(self):
        return f"Location: {self.street}"
    def __repr__(self):
        return f"Location: {self.street}"

class Human(ABC):
    def __init__(self,name: str,old: int):
        self.name = name
        self.old = old
        # print(str(self))

    def __str__(self):
        return f"Worker: {self.name},{self.old}"
    def __repr__(self):
        return f"Worker: {self.name},{self.old}"

    @abstractmethod
    def showInfo(self):
        return f"Имя: {self.name}, возраст: {self.old}"

    @abstractmethod
    def hello(self):
        return "Здравствуйте"

class LibraryWorker(Human):
    def __init__(self, name: str, old: int):
        super(LibraryWorker, self).__init__(name,old)
        self.salary = 30
        print(super(LibraryWorker, self).__str__())
        print(str(self))

    def __str__(self):
        return f"LibraryWorker(Worker): {self.name}, {self.old}, {self.salary}"
    def __repr__(self):
        return f"LibraryWorker(Worker): {self.name}, {self.old}, {self.salary}"

    def hello(self):
        print(super().hello()+f", меня зовут {self.name}, могу ли я Вам чем-то помочь?")

    def showInfo(self):

        print(super().showInfo() +f", зарплата: {self.salary}")

class Library:
    def __init__(self, title: str,booksNum: int,workers: list,status: bool,location: Location):
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
                if type(workers[i]) != LibraryWorker:
                    print("!параметр workers[] должен быть типа LibraryWorker!")
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

    @staticmethod
    def openingHours(openingTime: int):
        if openingTime > 20:
            print("Это слишком поздно для открытия библиотеки")
        finishTime = openingTime + 8
        if finishTime > 23:
            finishTime = 23
        return f"Открытие в {openingTime}. Закрытие в {finishTime}"

    def employeeSalary(numOfWorkers: int,salary: int):
        return f"Траты на зарплату для работников в месяц: {numOfWorkers * salary}"


def dumpInFile(obj):
    f = open(r"file.txt",'wb')
    pickle.dump(obj,f)
    f.close()

def loadFromFile():
    f = open(r"file.txt",'rb')
    new_obj = pickle.load(f)
    f.close()
    return new_obj



ane = LibraryWorker('Ane','21')
ane.hello()
ane.showInfo()

CheckStaticMethod = Library.openingHours(8)
print(CheckStaticMethod)

Library.employeeSalary = staticmethod(Library.employeeSalary)
print(Library.employeeSalary(3,30))