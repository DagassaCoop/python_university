import os

txt1 = open("./files_dir/txt1.txt",'w')
txt1.write("mother\nfather\n\nson\ndaughter")
txt1.close()
txt2 = open("./files_dir/txt2.txt",'w')
txt2.write("uncle\naunt\n\ngrandfather\ngrandmother")
txt2.close()

def task01(*args):
    """Функция что меняет содержимое местами в двух файлах с помощью файла посредника

    Аргументы:
    *args (any): Любой возможный аргумент

    Результат:
    None (none): Ничего не возвращает

    """
    try:
        txt1 = open("./files_dir/txt1.txt",'r')
        temp = open('./files_dir/temp.txt','w')
        temp.write(txt1.read())
        txt1.close()
        temp.close()
        filename = os.path.splitext(txt1.name)[0]
        print("\nRead from " + filename)
    except IOError:
        print("File not found or path is incorrect")
    finally:
        print("__exit_from_file__")

    try:
        txt2 = open("./files_dir/txt2.txt",'r')
        txt1 = open("./files_dir/txt1.txt",'w')
        txt1.write(txt2.read())
        txt2.close()
        txt1.close()
        filename = os.path.splitext(txt2.name)[0]
        print("\nRead from " + filename)
    except IOError:
        print("File not found or path is incorrect")
    finally:
        print("__exit_from_file__")


    try:
        temp = open("./files_dir/temp.txt",'r')
        txt2 = open("./files_dir/txt2.txt",'w')
        txt2.write(temp.read())
        filename = os.path.splitext(temp.name)[0]
        print("\nRead from " + filename)
        temp.close()
        txt2.close()
    except IOError:
        print("File not found or path is incorrect")
    finally:
        print("__exit_from_file__")


def task02(*args):
    """Функция что сравнивает длинну строк каждого файла

    Аргументы:
    *args (any): Любой возможный аргумент

    Результат:
    None (none): Ничего не возвращает

    """
    try:
        txt1 = open("./files_dir/txt1.txt",'r')
        text_txt1 = txt1.readlines()
        txt1.close()
        filename = os.path.splitext(txt1.name)[0]
        print("\nRead from " + filename)
    except IOError:
        print("File not found or path is incorrect")
    finally:
        print("__exit_from_file__")

    try:
        txt2 = open("./files_dir/txt2.txt",'r')
        text_txt2 = txt2.readlines()
        txt2.close()
        filename = os.path.splitext(txt2.name)[0]
        print("\nRead from " + filename)
    except IOError:
        print("File not found or path is incorrect")
    finally:
        print("__exit_from_file__")

    print(text_txt1)
    print(text_txt2)

    N = len(text_txt1)
    i=0
    for i in range(N):
        if len(text_txt1[i]) != len(text_txt2[i]):
            print("Error in line: "+str(i))
            break

# task01()
# task02()
help(task01)
help(task02)
