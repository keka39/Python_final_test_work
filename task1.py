# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, 
# редактированием и удалением заметок. 
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время 
# создания или последнего изменения заметки. 
# Сохранение заметок необходимо сделать в формате json или csv формат 
# (разделение полей рекомендуется делать через точку с запятой). 
# Реализацию пользовательского интерфейса студент может делать как ему удобнее, 
# можно делать как параметры запуска программы (команда, данные), 
# можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

import datetime

сейчас = datetime.datetime.now()

collect = {}
d = 1

with open("/Users/anastasiamamulat/Desktop/Python_final_task_work/Python_final_test_work/notes.csv", "r", encoding="utf-8") as file:
    for line in file:
        line = line.replace("\n", "").replace("ID: ", "")
        collect[d] = list(line.split("; "))
        d += 1

def findNotes(data):
    find = input("Введите запрос для поиска: ")
    for i in data:
        for j in range(len(data[i])):
            if find in data[i][j]:
                print(data[i])

def getNotes(data):
    for i in data:
        print(data[i])

def addNotes(data):
    topic = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    s = 1
    while True:
        if s in data:
            s += 1
        else:
            data[s] = [topic, body]
            break

def updateNotes(data):
    name = input("Введите заголовок и тело заметки для обновления: ")
    for i in data:
        if name in data[i]:
            new_data = input("Введите новые данные через пробел: ").split()
            data[i] = new_data

def deleteNotes(data):
    name = input("Введите заголовок для удаления: ")
    for i in list(data.keys()):
        if name in data[i]:
            del data[i]           

def choice(n, data):
    if n == 1:
        getNotes(data)
    elif n == 2:
        findNotes(data)
    elif n == 3:
        addNotes(data)
    elif n == 4:
        updateNotes(data)
    elif n == 5:
        deleteNotes(data)
    elif n == 0:
        return

while True:
    print("Здравствуйте! Выберите действие с заметками от 1 до 5:")
    print("1 - показать заметки")
    print("2 - произвести поиск по запросу")
    print("3 - добавить данные в заметки")
    print("4 - изменить данные в заметках")
    print("5 - удалить данные из заметок")
    print("0 - для выхода")
    n = int(input("Введите номер действия: "))

    if n == 0:
        break

    choice(n, collect)

with open("/Users/anastasiamamulat/Desktop/Python_final_task_work/Python_final_test_work/notes.csv", "w", encoding="utf-8") as file:
    for k in collect:
        file.write(f"ID: {k};{collect[k][0]};{collect[k][1]};{сейчас}\n")

print(collect)