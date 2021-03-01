# file = open('1.txt')
# for line in file:
#     print(line.strip())
#
# file2 = open('2.txt', 'w', encoding='UTF-8')  # создать файл 2.txt
# file2.write('add note to file')  # добавляется запись в файл
# file2.close()  # файл сохраняется и закрывается

# file = open('D:\питон\упражнения\salary.txt', 'r')
# file.seek(0)
# print(file.readlines())
# file.close()

# import os
# file_path = 'D:\\питон\\Книги\\Data analysis.pdf'
# print(file_path)
# print(os.path.split(file_path))
# print(file_path.split(os.path.sep))
#
# print(os.path.getsize('D:\\питон\\Книги\\Data analysis.pdf'))
#
# print(os.listdir('D:\\питон\\Книги\\'))
#
# total_size = 0
# for file_name in os.listdir('D:\\питон\\Книги\\'):
#     total_size = total_size + os.path.getsize(os.path.join('D:\\питон\\Книги\\'))
# print(total_size)

# file = open('D:\\питон\\обучение\\инструкции, циклы, функции, модули и т.д\\ggg.txt', encoding='UTF-8')
# print(file.read())
# file.close()
file = open('D:\\питон\\обучение\\инструкции, циклы, функции, модули и т.д\\ggg.txt', 'a', encoding='UTF-8')
file.seek(0)
file.write('rrrНачало\n')
file.close()
file = open('D:\\питон\\обучение\\инструкции, циклы, функции, модули и т.д\\ggg.txt', encoding='UTF-8')
print(file.read())
file.close()



import csv
with open("D:\\Python projects\\обучение\\1.csv", "w", encoding='utf-8') as w_file:
    names = ["Name", "Age", "Height"]
    file_writer = csv.DictWriter(w_file, delimiter=";", lineterminator="\n", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerows([{"Name": "Alex", "Age": "23", "Height": "184"},
                           {"Name": "Tom", "Age": "35", "Height": "170"},
                           {"Name": "Tim", "Age": "21", "Height": "178"}])


with open("D:\\Python projects\\обучение\\1.csv") as crime:
    file_reader = csv.DictReader(crime, delimiter=";")
    for line in file_reader:
        print(line['Name'], line['Age'], line['Height'])