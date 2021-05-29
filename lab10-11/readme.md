# Лабораторна робота №10-11

# Наслідування та поліморфізм у Python

# Завдання

Використовуючи створені класи розширити попередню ЛР таким чином:
1. Створити ієрархію класів. Додати до ієрархії класів хоча б один 
абстрактний клас (не менше двох абстрактних методів).
2. У похідному класі/класах (класі-насліднику) додати змінну класу (class
variable). Продемонструвати різницю між змінними класу та екземпляра.
3. Додати статичні методи та методи класу. 
4. Обробити можливі помилки, розробивши власну ієрархію виключень.
* у разі потреби можна змінювати структуру базового класу із попередньої 
ЛР

# Опис Функціональних вимог:

Новий абстрактний клас - Human(ABC)

    def __init__(self,name: str,old: int):
        self.name = name
        self.old = old

Є родичем для класу LibraryWorker, має такі абстрактні методи: showInfo та hello, один виводіть інформацію о люди, а інший емулює вітання.

У класі насліднику демострується різниця між класами наступним чином:

    def __init__(self, name: str, old: int):
        super(LibraryWorker, self).__init__(name,old)
        self.salary = 30
        print(super(LibraryWorker, self).__str__())
        print(str(self))

Було додано наступні статичні методи: openingHours та employeeSalary

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


# Приклад вхідних даних:

openingHours:

    CheckStaticMethod = Library.openingHours(8)

employeeSalary:

    Library.employeeSalary = staticmethod(Library.employeeSalary)