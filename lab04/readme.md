# Лабораторна робота №4 

# Тема: Кортежі та cловники

# Завдання

Загальне завдання.
Відповідно до свого варіанту
- визначити умови;
- написати програму, яка розв’язує завдання;
- для подання необхідної інформації реалізувати певну структуру даних, під
час визначення якої використовувати будь-які комбінації вбудованих
об’єктів (кортежі, словники, списки, рядки); спробуйте звернутися до
окремих елементів;
- реалізувати a) режим виведення всіх значень словника; б) додавання
(видалення) нового запису до (зі) словника; в) режим перегляду вмісту
словника за відсортованими ключами (перетворити об’єкт подання ключів в
список);
- для генерації тестових даних використовувати модуль Random;
- при написанні програми використовувати техніки «чистого» писання коду
мовою Python.

Задано дані про кількість опадів, які випали за кожен день місяця, і про
температуру повітря в ці дні. Скласти програму, що визначає, яка кількість
опадів випала у вигляді снігу і яка – у вигляді дощу (вважати, що дощ іде, якщо
температура повітря вище 0° С).


# Опис Функціональних вимог:

На початку створюється декілька змінних: 
N = 31;
i = 0;
mounth = [];
water = 0;
show = 0;
Через цикл while заповнюємо массив mounth обїектами типу dict (словник): 

day = {"day": i+1,"precipitation": random.randint(-10,10),"C*":random.randint(-25,25)}

За допомогою механізму розгалудження коду розраховуємо кількість опадів снігу та дощу для індивідуального завдання.
Використовуючи функції масивів pop() та push() спочатку видаляємо, а потім додаємо обїєкт списку за індексом delete_day_index.
Використовуємо фукнції sorted() для сортуванням масиву по ключу "C*" 

# Приклад вхідних даних:

Вхідні дані потрібні лише для частини (б), потрібно ввести індекс дня, який ви хочете видалити зі списку, а потім повернути. Напириклад: delete_day_index = 4