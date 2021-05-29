# Лабораторна робота №12

# Ітератори та генератори Python

# Завдання

Використовуючи попередню ЛР розширити її таким чином:
1. Додати ітератор на основі класу, що зможе працювати із класаминаслідниками.
2. Додати генератор у класс-наслідник.
3. Оновити метод зчитування із файла, написати власний менеджер 
контексту, що буде здатний зчитувати із файлу дані та повертати список 
об’єктів класу-наслідника

# Опис Функціональних вимог:

Iterator:

    class Iterator:
        def __init__(self, _list):
            self.list = _list
    
        def __iter__(self):
            self.i = 0
            return self
    
        def __next__(self):
            if self.i < len(self.list):
                res = self.list[self.i]
                self.i += 1
                return res
            else:
                raise StopIteration

Generator:

    class Generator(Iterator):
        def generate(self, it):
            for self.it in self.list:
                yield self.it


# Приклад вхідних даних:


Початкові дані:

    lib = Library("Micko",2000,[bob,ane],True,Location("Kharkiv 4"))

Для використання ітератору необхідно створити нову змінну типу Iterator та передати туди масив:

    iter = Iterator(lib.workers)
    print('iter: ')
    for i in iter:
        print(i)

Для використання генератору необхідно створити нову змінну типу Generator, передати туди масив та викликати метод generate і передати туди ітератор. 

    gener = Generator(lib.workers)
    print('generator: ')
    for i in gener.generate(iter):
        print(i)