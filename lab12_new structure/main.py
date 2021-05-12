import pickle
from abc import ABC, abstractmethod

class Book:
    def __init__(self,title: str, author: str,year_writing: int,genre: str):
        self.title = title
        self.author = author
        self.year = year_writing
        self.genre = genre

    def __str__(self):
        return f"Book: {self.title}, {self.author}, {self.year}, {self.genre}"
    def __repr__(self):
        return f"Book: title, author, year, genre"

class Library(ABC):
    def __init__(self,title: str,books: list):
        self.title = title
        self.books = books

    def __str__(self):
        return f"Library: {self.title},{self.books}"
    def __repr__(self):
        return f"Library: title, books"

    @abstractmethod
    def checkBook(self,bookTitle):
        for i in self.books:
            if i.title == bookTitle:
                book = i
        print(book)
        str(book)

    def __iter__(self):
        return iterator(self)

class OnlineLibrary (Library):
    def __init__(self,title, books:list, domain):
        super(OnlineLibrary, self).__init__(title,books)
        self.domain = domain

    def __str__(self):
        return f"OnlineLibrary(Library): {self.title}, {self.books}, {self.domain})"
    def __repr__(self):
        return f"OnlineLibrary(Library): title, books, domain)"

    def checkBook(self,bookTitle):
        super(OnlineLibrary, self).checkBook(bookTitle)


class iterator():
    def __init__(self,data):
        self.counter = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.data):
            self.counter+=1
            return self.data[self.counter-1]
        else:
            raise StopIteration

class generator():
    def __init__(self,data):
        self.counter = 0
        self.data = data

    def __iter__(self):
        while self.counter < len(self.data):
            yield self.data[self.counter]
            self.counter+=1

def dumpInFile(obj):
    f = open(r"file.txt",'wb')
    pickle.dump(obj,f)
    f.close()

def loadFromFile():
    f = open(r"file.txt",'rb')
    new_obj = pickle.load(f)
    f.close()
    return new_obj




def main():
    BOOKSNUM = 5 # количество книг
    books = [] # книги

    for i in range(BOOKSNUM):
        book = Book(f'book{i + 1}', f'author{i + 1}', 2000, 'happy')
        books.append(book)

    lib = OnlineLibrary('Mino', books, 'http')

    iter = iterator(lib.books)
    while True:
        try:
            print(iter.__next__())
        except StopIteration as e:
            break
    print('\n')
    gener = generator(lib.books)
    for i in gener:
        print(i)

    dumpInFile(lib)
    newLib = loadFromFile()
    print('\n'+repr(newLib))


main()

