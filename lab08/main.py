import os
import shutil

txt1_path = "./files_dir/txt1.txt"
txt2_path = "./files_dir/txt2.txt"
txt1 = open(txt1_path,'w')
txt1.write("mother\nfather\n\nson\ndaughter")
txt1.close()
txt2 = open(txt2_path,'w')
txt2.write("uncle\naunt\n\ngrandfather\ngrandmother")
txt2.close()

def showFiles(*args):
    """Функция, что выводит в консоль содержимое файла/файлов

    Аргументы:
    *args (String): Путь к файлу

    Результат:
     None (none): Ничего не возвращает, так как выводит информацию в консоль
    """
    for arg in args:
        try:
            file = open(arg,'r')
            print(file.read())
            print('\n')
        except:
            file.close()
            print("File not found or path is incorrect")
    print('\n')



def task01(*args):
    """Функция что меняет содержимое местами в двух файлах с помощью файла посредника

    Аргументы:
    *args (any): Любой возможный аргумент

    Результат:
    None (none): Ничего не возвращает

    """
    try:
        print('Before swap:'+'\n')
        showFiles(txt1_path,txt2_path)
        temp_path = shutil.copyfile(txt2_path,"./files_dir/temp.txt")
        shutil.copyfile(txt1_path,txt2_path)
        shutil.copyfile(temp_path,txt1_path)
        print('After swap:'+'\n')
        showFiles(txt1_path, txt2_path)
        os.remove(temp_path)
    except:
        print("File not found or path is incorrect")
    finally:
        print("__Finish__")




def task02(*args):
    """Функция что сравнивает длинну строк каждого файла

    Аргументы:
    *args (any): Любой возможный аргумент

    Результат:
    None (none): Ничего не возвращает

    """
    try:
        file1 = open(txt1_path,'r')
        file2 = open(txt2_path,'r')
        i = 0
        while True:

            lineFile1 = file1.readline()
            lineFile2 = file2.readline()

            if not lineFile1:
                print("\nExit\n")
                break
            else:
                print("line " + str(i) + " from file1: " + lineFile1)
                print("line " + str(i) + " from file1: " + lineFile2)
                if len(lineFile1) != len(lineFile2):
                    print("Does not match in string: " + str(i)+"\n")
                    print("\nExit\n")
                    break
            i += 1
    except:
        print("File not found or path is incorrect")
    finally:
        file1.close()
        file2.close()


# task01()
# task02()
# help(task01)
# help(task02)
