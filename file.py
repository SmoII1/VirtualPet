# a = open("main.py", "r", encoding="UTF-8")
# b = a.readlines()
# n = 1
# for c in b:
#     print(n, c, end="")
#     n = n+1
# a = open("test.py", "w", encoding="UTF-8")
# a.write("a = 0\n")
# a.write("b = 2.000004\n")
# a.close()
# a = open("test.py", "a", encoding="UTF-8")
# a.write("a = 'ffffffffffffff'\n")
# a.write("b = []\n")
# a.close()
# a = 1
# while a == 1:
# print("Меню: 1.показать содержимое файла с нумерацией, 2.создать файл и записать в него текст, 3.Добавить текст в файл, 4. Выйти из программы")
# l = int(input("Выберите действие "))

# if l == 1:
#     n = 1
#     filename = str(input("Какой файл вы хотите открыть? "))
#     file = open(filename, "r", encoding="UTF-8")
#     filer = file.readlines()
#     for c in filer:
#         print(n, c, end="")
#         n = n+1

# if l == 2:
#     filename2 = input("Придумайте название файла ")
#     filetekst2 = input("Какой текст вы хотите написать в файле ")
#     file2 = open(filename2, "w", encoding="UTF-8")
#     file2.write(filetekst2)
#     file2.close()

# if l == 3:
#     filename3 = input("Выберете файл в который хотите добавить текст ")
#     filetekst3 = input("Какой текст вы хотите добавить в файл ")
#     file3 = open(filename3, "a", encoding="UTF-8")
#     file3.write(filetekst3)
#     file3.close()

# if l == 4:
#     a = 4
#     print("Вы вышли из программы")

# def copy_file(filename):
#     file = open(filename, "r", encoding="UTF-8")
#     b = file.read()
#     file.close()
#     c = filename.find(".")
#     filecopy = open(filename[0:c] + " copy" + filename[c:], "w", encoding="UTF-8")
#     filecopy.write(b)
#     filecopy.close()
# a = copy_file("main.py")
# a = open("numbers.txt", "r", encoding="UTF-8")
# b = a.readlines()
# d = []
# for c in b:
#     n = int(c)
#     d.append(n)
# d.sort()
# m = open("numbers.txt", "w", encoding="UTF-8")
# for v in d:
#     m.write(str(v)+"\n")
# m.close()
# def fynkchia(filename, bykva):
#     a = open(filename, "r", encoding="UTF-8")
#     b = a.readlines()
#     n = 1
#     for c in b:
#         if bykva in c:
#             return n
#         n = n+1
# m = fynkchia("main.py", ":")
# print(m)
# def nn(filename, text):
#     a = open(filename, "r", encoding="UTF-8")
#     b = 0
#     for line in a.readlines():
#         if text in line:
#             b = b + 1
#     return b

# c = nn("main.py", "pass")
# print(c)
import json
# a = {"Влад": "+8888888888", "Макар": "+999999999"}
# b = open("nnn.json", "w", encoding="UTF-8")
# json.dump(a, b, ensure_ascii=False, indent=4)
a = open("nnn.json", "r", encoding="UTF-8")
b = json.load(a)
print(b)
