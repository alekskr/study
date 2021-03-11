import tkinter as tk
import random


def say_hello():
    print('hello')


def counter():
    global count
    count += 1
    btn4['text'] = f'Счетчик: {count}'


def add_label():
    label_2 = tk.Label(win, text='123')
    label_2.pack()


def disabled():
    global count_btn2
    if count_btn2 % 2 == 0:
        btn2['state'] = tk.DISABLED
        count_btn2 += 1
    else:
        btn2['state'] = tk.NORMAL
        count_btn2 += 1


def change_bg():
    i = ('#ffe6e6', '#bfff00', '#00bfff', '#936c6c', '#ffcccc')
    win['bg'] = random.choice(i)


count = 0
count_btn2 = 0

win = tk.Tk()  # создание главного окна, вызов класса TK
win.title('First App')  # изменение заголовка
win.geometry('500x600+300+150')  # размеры окна (длинаxширина) и
# +100 вправо +100 вниз расположение окна относительно верхнего левого угла
win.resizable(True, True)  # растягивание окна (по умолчанию стоит (True, True) - высота и ширина)
win.minsize(200, 400)  # минимальный размер окна
win.maxsize(600, 700)  # минимальный размер окна

photo = tk.PhotoImage(file='fun.png')  # подгрузка класса PhotoImage для смены иконки
win.iconphoto(False, photo)  # прикрепление картинки к окну

win.config(bg='#e6fff3')  # изменение цвета фона background сокращенно bg. Цвет можно писать либо по-англ, например,
# red, либо при помощи модели rgb.


# ВИДЖЕТЫ
# 1 Label - отображение текстовой ирформации
# параметры:
# 1.расположение (окно win),
# 2.текст,
# 3.цвет фона,
# 4.fg - font ground - цвет текста,
# 5.font - шрифт и кортеж из трех значений (шрифт, размер, обычный/жирный/наклонный),
# 6.отступы текста внутри виджета: padx по иксу слева и справа от надписи, pady по игреку,
# 7.ширина width и высота height виджета в количестве знаков
# 8.anchor расположение текста n=north, s=south, e=east, w=west, ne, nw, se, sw
# 9.relief границы, значение RAISED оздает полутень, bd - толщина границы
# 10. justify выравниевание текста, значения LEFT и RIGHT, по умолчание justify=tk.CENTER
label_1 = tk.Label(win,
                   text='''HELLO!
WORLD!''',
                   bg='#cccc33',
                   fg='#cc3333',
                   font=('Arial', 15, 'bold'),
                   padx=10, pady=10,
                   # width=20, height=10,
                   anchor='sw', bd=10, relief=tk.RAISED,
                   justify=tk.LEFT)

btn1 = tk.Button(win,
                 text='hello', bg='orange',
                 command=disabled  # скобки функции не указывать
                 )
btn2 = tk.Button(win, text='btn2', command=add_label)
btn3 = tk.Button(win, text='btn3', command=lambda: tk.Label(win, text='lambda').pack())
btn4 = tk.Button(win, text='Счетчик {}'.format(count), command=counter, bg='red', activebackground='blue',
                 state=tk.NORMAL)  # счетчик нажатия на кнопку. state - состояние NORMAL, DISABLED
btn5 = tk.Button(win, text='change color', command=change_bg)

label_1.pack()  # расположение виджета Label
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

win.mainloop()  # главный цикл, запускает окно приложения


# Какие шрифты можно использовать
# import tkinter.font as tkFont
# print(tkFont.families(tk.Tk()))

# ctrl + нажать на функцию или метод - информация
