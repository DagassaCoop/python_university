# Лабораторна робота №13-14

# Збір даних з веб-документів за допомогою Python. Робота з API. Бібліотека Pandas

# Завдання

Реалізуйте програму, яка для заданих сайтів отримує інформацію. 
Використати API та парсинг html сторінок за допомогою Beautiful Soup. 
Додати обробку пагінації сторінок. Порівняти два підходи. Обробити та 
зберегти інформацію у .csv файл використовуючи Pandas. Передбачити бан 
(avoid getting banned) зі сторони сервера та імплементувати техніки, що 
дозволяють зменшити його можливість. При виконанні завдання 
використовувати отримані знання у попередніх темах (функції, класи, 
датакласи та ін.)

4. https://ua.jooble.org/
А) Використовуючи API:Для заданих запитів (наприклад Python, Java) та дат отримати вакансії 
(назва, заробітна плата, опис, компанія, локація).
Б) Використовуючи Beautiful Soup:
Отримати всі поточні вакансії із запитом Data Scientist та заробітною 
платою від 16.000 гривень. Приклад посилання: 
https://ua.jooble.org/SearchResult?ukw=data%20scientist .


# Опис Функціональних вимог:

Для виконання даної роботи було створено клас Article у який записувалися отримані дані з сайту.
Для отримання результату було використано бібліотеки BeautifulSoup та requests. Для зберігання використовувався pandas.
Отримання даних (класи було знайдено на сайті, через інструмент перегляду коду сторінки.:

    soup =  bs(response.text,'lxml')
    titles = soup.find_all('span', class_='_1b9db')
    companies = soup.find_all('p', class_='e2601')
    descriptions = soup.find_all('div', class_='_10840')
    prices = soup.find_all('p', class_='  ')
    locations = soup.find_all('div', class_='caption d7cb2')

Функція createArticlesArr(titles,compaties,descriptions,prices,locations) потрібна для створення об'єктів типу Article та запису іх у один массив article.

У функції init() виконується сортування та отримання фінального масиву.

У функції articleInDataFrame(articles) виконується перетворення массиву із Article у DataFrame та запис інформації у файл типу csv.

# Приклад вхідних даних:

Запит на підключення:

    URL = 'https://ua.jooble.org/SearchResult?ukw=data%20scientist'
    response = requests.get(URL)
    soup =  bs(response.text,'lxml')

Виклик виконуючих функцій:

    createArticlesArr(titles,companies,descriptions,prices,locations)
    init()