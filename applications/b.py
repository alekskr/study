# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(111, 14, 151, 61))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(332, 12, 375, 192))
        self.tableWidget.setMinimumSize(QSize(350, 180))
        self.tableWidget.setMaximumSize(QSize(375, 16777215))
        self.tableWidget.setStyleSheet(u"gridline-color: rgb(255, 33, 140);\n"
"\n"
"\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(330, 250, 350, 271))
        self.tabWidget.setMinimumSize(QSize(350, 180))
        self.tabWidget.setMaximumSize(QSize(375, 16777215))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 351, 211))
        self.label_2.setPixmap(QPixmap(u"fall.jpg"))
        self.label_2.setScaledContents(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget = QWidget(self.tab_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 331, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnmess = QPushButton(self.verticalLayoutWidget)
        self.btnmess.setObjectName(u"btnmess")

        self.verticalLayout.addWidget(self.btnmess)

        self.plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayoutWidget_2 = QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 9, 394, 269))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dateTimeEdit = QDateTimeEdit(self.verticalLayoutWidget_2)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.verticalLayout_2.addWidget(self.dateTimeEdit)

        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(11, 52, 93, 28))
        self.pushButton_2.setMinimumSize(QSize(90, 28))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(11, 14, 93, 28))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(11, 90, 90, 28))
        self.comboBox.setMinimumSize(QSize(90, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(statustip)
        self.action_exit.setStatusTip(QCoreApplication.translate("MainWindow", u"wwww", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0442\u0438\u043d\u043a\u0430", None))
        self.btnmess.setText(QCoreApplication.translate("MainWindow", u"QMessageBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Element1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Element2", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0415\u0449\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

