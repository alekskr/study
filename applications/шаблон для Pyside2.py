# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide2 import QtWidgets
from file_name import Ui_MainWindow
import sys

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()



if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)  # настройки компьютера, на котором запускается проект
    # Сздание инстанса класса
    example = MyApp()  # создание основного окна на основе класса MyApp
    # Запуск
    sys.exit(app.exec_())
