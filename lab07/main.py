from datetime import datetime
import time
import random

def decorator_datatime(function):
    """Декроратор для измерения времени работы функции

    Аргументы:
    function (function): Функия на которой будет использоваться декоратор

    Результат:
    wrapper (function): Функция внутри декоратора (тело и логика декоратора)

    """
    def wrapper(*arguments):
        """Функция внутри декоратора (Основное тело и логика)

        Аргументы:
        arguments (any): Переменная, которая что-то содержит

        Результат:
        func (function): Возвращает входящую вункцию в виде переменной

        """
        start_time = datetime.now()
        func = function(*arguments)
        time.sleep(1)
        end_time = datetime.now()
        print("Function's work time: " + str(end_time-start_time))
        return func

    return wrapper

def decorator_probabilities(function):
    """Декроратор для измерения времени работы функции

        Аргументы:
        function (function): Функия на которой будет использоваться декоратор

        Результат:
        wrapper (function): Функция внутри декоратора (тело и логика декоратора)

        """
    def wrapper(*arguments):
        """Функция внутри декоратора (Основное тело и логика)

        Аргументы:
        arguments (any): Переменная, которая содержит что-то

        Результат:
        func (function): Возвращает входящую вункцию в виде переменной
        wrapper (function): Вызывает саму себя для рекурсии

        """
        func = function(*arguments)
        p = random.randint(1,10)
        print(p)
        if p == 1 or p == 3 or p == 5 or p == 7 or p == 9:
            print("Complete")
            return func
        else:
            print("Fail")
            return wrapper(*arguments)
    return wrapper

def decorator_registered(function):
    """Декроратор для добавления использованных функций в общий список

        Аргументы:
        function (function): Функия на которой будет использоваться декоратор

        Результат:
        wrapper (function): Функция внутри декоратора (тело и логика декоратора)

        """
    def wrapped(*arguments):
        """Декроратор для добавления использованных функций в общий список

        Аргументы:
        arguments (any): Переменная, которая содержит что-то

        Результат:
        func (function): Возвращает входящую вункцию в виде переменной

        """
        func = function(*arguments)
        global REGISTERED
        N = len(REGISTERED)
        i = 0
        for i in range(N):
            if function.__name__ == REGISTERED[i]:
                return func
            i=i+1
        REGISTERED.append(function.__name__)
        return func
    return wrapped

REGISTERED = []

@decorator_probabilities
@decorator_datatime
@decorator_registered
def say_hi(arg1,arg2):
    return "\nMy name is {0} and i'm {1}".format(arg1,arg2)


@decorator_registered
def test1():
    return None

@decorator_registered
def test2():
    return None

print(say_hi("Dima","Student"))
test2()
test1()
test2()
print(REGISTERED)

# help(decorator_datatime)
# help(decorator_datatime(test1))
# help(decorator_registered)
# help(decorator_registered(test1))
# help(decorator_probabilities)
# help(decorator_probabilities(test1))