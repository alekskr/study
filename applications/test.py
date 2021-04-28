#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMessageBox
from b import Ui_MainWindow
import sys


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_click)
        self.pushButton_2.clicked.connect(self.btn2_click)
        self.btnmess.clicked.connect(self.qmessage_box)  # нажатие кнопки вызывает окно с сообщением
        self.checkBox.clicked.connect(self.check_box)
        self.combobox()
        self.table_1()
        self.main_menu()
        self.show()

    def main_menu(self):
        # exitAction = QAction('&Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(app.quit)
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAction)
        self.action_exit.triggered.connect(lambda: app.quit())
        self.action.triggered.connect(lambda: self.label.setText('вставлена запись'))
        self.action_3.triggered.connect(lambda: self.label.setText('кнопка действие'))

    def btn_click(self):
        self.label.setText('kyky')

    def btn2_click(self):
        a = ''
        for i in range(self.comboBox.count()):
            print(self.comboBox.itemText(i))
            a = a + self.comboBox.itemText(i) + '\n'
        self.label.setText('Состав:' + '\n' + a)

    def qmessage_box(self):  # функция выводит окно с сообщением
        message = QMessageBox()
        message.setWindowTitle('Help')
        message.setText('Пока эта кнопка в разработке')
        message.setIcon(QMessageBox.Warning)  # .Information, .Question, .Reset, .Cancel
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)  # добавление кнопок
        message.setInformativeText('setInformativeText')
        message.setDetailedText('Здесь отображается дополнительная информация')
        message.buttonClicked.connect(self.popup_action)  # метод, который обрабатывает нажатие
        # на кнопку в окне MessageBox

        message.exec_()

    def popup_action(self, btn):
        if btn.text() == 'OK':
            print('нажата кнопка Ок')
            self.label.setText('нажата кнопка Ок')
        elif btn.text() == 'Close':
            print('Нажата кнопка Close')
            self.label.setText('нажата кнопка Close')

    def check_box(self):
        self.plainTextEdit.clear()
        # if QtCore.Qt.Checked:
        #     self.plainTextEdit.clear()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_1:
            self.label.setText('1')
        if event.key() == QtCore.Qt.Key_F12:
            self.close()

    def combobox(self):
        self.comboBox.addItem('повар')
        self.comboBox.addItem('инженер')
        self.comboBox.addItem('водитель')

    def table_1(self):
        data = [('VW', '2008', '12.350'),
                ('BMW', '2005', '10.000'),
                ('Audi', '2015', '15.000'),
                ('Lada', '2020', '17.500')]
        columns = ('Марка', ' Год выпуска', 'Цена, $')
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)  # заголовки столбцов
        row = 0
        for i in data:
            column = 0
            for j in i:
                info = QtWidgets.QTableWidgetItem(j)
                # режим только для чтение:
                info.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                self.tableWidget.setItem(row, column, info)
                column += 1
            row += 1
        # сортировку надо вставлять после заполнения таблицы
        self.tableWidget.sortItems(0)  # сортировка таблицы по возрастанию первого столбца
        self.tableWidget.setSortingEnabled(True)  # сделать таблицу сортируемой по убыванию/возрастанию


if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)  # настройки компьютера, на котором запускается проект
    # Сздание инстанса класса
    example = MyApp()  # создание основного окна на основе класса MyApp
    # Запуск
    sys.exit(app.exec_())
