from PyQt5 import QtWidgets  # класс позволяет создавать виджеты (кнопки, надписи, формы)
from PyQt5.QtWidgets import QApplication, QMainWindow  # с помощью QApplication создается приложение,
# а с помощью QMainWindow создается окно. Суть в том, что одно приложение может содержать множество окон
import sys


class Window(QMainWindow):  # создаем класс для взаимодействия окна с различными объектами.
    # В скобках указывает QMainWindow - это значит, что наследует всё от этого класса
    def __init__(self):  # создаем конструктор
        super(Window, self).__init__()  # вызываем конструктор из родительского класса. В качестве параметра указываем
        # название нашего класса Window

        self.setWindowTitle('Простая программа')  # заголовок окна
        self.setGeometry(300, 250, 400, 200)  # здесь можно указать ширину и высоты окна и его смещение.
        # Первые да параметра - это смещение окна от левого верхнего угла

        self.main_text = QtWidgets.QLabel(self)  # self вначале говорит, что этот объект принадлжеит данному классу.
        # Второй self значит, что данная текстовая надпись будет принадлежать всему этому окну
        self.main_text.setText('Это базоая надпись')
        self.main_text.move(100, 100)  # позволяет двигать текст в пределах окна
        self.main_text.adjustSize()  # подстраивает ширину объекта под его содержимое

        self.btn = QtWidgets.QPushButton(self)  # создание кнопки
        self.btn.move(70, 150)  # сдвинуть на пиксели по иксу и по игреку относительно левого верхнего угла window
        self.btn.setText('Нажми на меня')
        self.btn.setFixedWidth(200)  # ширина кнопки
        self.btn.clicked.connect(self.add_label)  # присоединение (connect) к методу clicked (нажатие) другого метода,
        # который записывается без скобок

        self.new_text = QtWidgets.QLabel(self)  # создание объекта, который будет показываться при нажатии на кнопку

    def add_label(self):  # создание метода, который будет срабатывать при нажатии на кнопку
        self.new_text.setText('Вторая надпись')
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def application():  # создание основной функции
    app = QApplication(sys.argv)  # новый экземпляр QApplication и настройки компьютера, на котором
    # запускается проект
    window = Window()  # создание объекта класса

    window.show()  # метод показывает окно
    sys.exit(app.exec_())  # Запуск приложения


if __name__ == '__main__':
    application()
