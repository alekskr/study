# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
from PySide2.QtCore import Slot
import sys


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()  # параметры передаваемые в родительский конструктор
        self.setWindowTitle('Редактор кода')
        self.setGeometry(300, 250, 350, 200)
        self.text_edit = QtWidgets.QTextEdit(self)  # добавление внутрь окна объекта TextEdit
        self.setCentralWidget(self.text_edit)  # метод, с помощью которго указываем центральный виджет, который
        # будет занимать всё окно

        self.create_menu_bar()  # создаем метод, с помощью которого создаем меню

    def create_menu_bar(self):
        self.menu_bar = QMenuBar(self)  # создаем глобальный объект меню
        self.setMenuBar(self.menu_bar)  # обращаемся к самому окну и указываем что у окна будет меню - объект menu_bar

        # добавление элементов внутри меню:
        fileMenu = QMenu('&Файл', self)  # для создания элеметов в меню
        editMenu = QMenu('&Edit', self)
        self.menu_bar.addMenu(fileMenu)
        self.menu_bar.addMenu(editMenu)

        fileMenu.addAction('Открыть', self.action_clicked)  # добавление пункта меню при нажатии на который будет
        # происходить действие. в качестве параметров указываем название пункта меню и метод который будет
        # срабатывать при нажатии
        fileMenu.addAction('Сохранить', self.action_clicked)
        fileMenu.addAction('Выход', self.action_clicked)
        editMenu.addAction('Вставить Default text', self.action_clicked)
        editMenu.addAction('Очистить', self.action_clicked)

        # open_file = fileMenu.addMenu('&Открыть')  # добавление подпункта меню
        # save_file = fileMenu.addMenu('&Сохранить')

    @Slot()  # анотация которая обрабатывает нажатия на пункты меню
    def action_clicked(self):
        action = self.sender()  # получение информации относительно того объекта на который нажали
        print('Action: ' + action.text())
        if action.text() == 'Открыть':
            file_name = QFileDialog.getOpenFileName(self)[0]  # [0] - открываем первый выбранный файл
            try:
                with open(file_name, 'r', encoding='UTF-8') as file:
                    self.text_edit.setText(file.read())
            except FileNotFoundError:
                print('No such file')

        elif action.text() == 'Сохранить':
            file_name = QFileDialog.getSaveFileName(self)[0]  # [0] - сохраняем первый выбранный файл
            try:
                with open(file_name, 'w', encoding='UTF-8') as file:
                    text = self.text_edit.toPlainText()  # toPlainText возвращает весь текст который записан в
                    # текстовом поле
                    file.write(text)
            except FileNotFoundError:
                print('No such file')

        elif action.text() == 'Выход':
            quit()

        elif action.text() == 'Вставить Default text':
            self.text_edit.setText('Default text')

        elif action.text() == 'Очистить':
            self.text_edit.clear()


def application():
    # метод, который будет вызываться при запуске файла
    app = QApplication(sys.argv)  # настройки компьютера, на котором запускается проект
    window = MyApp()  # создание основного окна на основе класса Window
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':  # если это основной файл, который будем запускать, то сразу будет запускаться
    # метод application()
    application()
