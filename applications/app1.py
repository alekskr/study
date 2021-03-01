import tkinter as tk

win = tk.Tk()  # создание главного окна, вызов класса TK
win.title('First App')  # изменение заголовка
win.geometry('500x600+100+100')  # размеры окна (длинаxширина) и
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
                   anchor='sw',
                   relief=tk.RAISED, bd=10,
                   justify=tk.LEFT)
label_1.pack()  # расположение виджета Label

win.mainloop()  # главный цикл, запускает окно приложения


# Какие шрифты можно использовать
# import tkinter.font as tkFont
# print(tkFont.families(tk.Tk()))
