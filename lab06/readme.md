# Лабораторна робота №6

# Функції

# Завдання 

Завдання 1. Загальне завдання:
Розробіть функції для здійснення наступних операцій зі списками:
1. Швидке сортування;
2. Пошук елементу за значенням;
3. Пошук перших 𝑛 мінімальних елементів;
4. Пошук перших 𝑛 максимальних елементів;
5. Пошук середнього арифметичного;
6. Повернення списку, що сформований з початкового списку, але не містить
повторів (залишається лише перший з однакових елементів).
Зробити описи Doc strings для кожної реалізованої функції

Завдання 2 (варіант 4): 

Розробити функції відповідно до варіанту. Зробити описи Doc
strings для кожної реалізованої функції. Передбачити параметри за
замовчуванням.

# Опис Функціональних вимог:

Функція "queckSort": Використана функція для сортування масивів .sort().

Функція "valueSearch": Функція у циклі порівнює значення із значеннями масиву.

Функція "findMinN": Відсортувавши масив функцією queckSort додаємо у фінальний масив вказану кількість елементів починаючи с першої осередки.

Функція "findMaxN": Відсортувавши масив функцією queckSort додаємо у фінальний масив вказану кількість елементів починаючи с останньої осередки.

Функція "findAverage": Сумуємо усі елементи та ділимо на їх кількість.

Функція "onlyOne": Функція перебирає усі значення через масив, використовуючи функцію .count() визначає кількість таких елементів у масиві. Якщо таких елементів більше 1, то за допомогою функції .index() визначає перший елемент і якщо зараз цикл масиву на ньому то додає його у фінальний масив.

# Приклад вхідних даних:

queckSort(arr)
    Фунція для швидкого сортування.
    
    
    Аргументи:
    arr (list): Массив чисел.
    
    
    Результат:
    new_arr (list): Відсортований масив чисел.


valueSearch(arr, value)
    Функція для пошуку індекса числа.
    
    
    Аргументи:
    arr (list): Масив чисел.
    value (int): Число індекс якого потрібно знайти.
    
    
    Результат:
    i (int): Індекс числа, яке було задано.
    "Value not find" (str): Результат, якщо такого числа немає в масиві.


findMinN(arr, num)
    Функція для мошуку найменших значень.
    
    
    Аргументи:
    arr (list): Масив чисел.
    num (int): Кількість найменших чисел.
    
    
    Результа:
    finish_arr (list): Масив, що містить найменші числа.


findMaxN(arr, num)
    Функція для пошуку найбільших чисел.
    
    
    Аргументи:
    arr (list): Масив чисел.
    num (int): Кількість найменших чисел.
    
    
    Результат:
    finish_arr (list): Масив, що містить найбільші числа.


findAverage(arr)
    Функція для пошуку середнього арифметичного.
    
    
    Аргументи:
    arr (list): Масив чисел.
    
    
    Результат:
    result (int): Середнє арифметичне.


onlyOne(arr)
    Функція для очищеня масиву від дублюючих значень.
    
    
    Аргументи:
    arr (list): Масив чисел.
    
    
    Результат:
    new_arr (list): Очищений від дублів масив чисел.
