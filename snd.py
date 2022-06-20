from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
from kayak_f import search_button


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 515)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo_from_city = QtWidgets.QComboBox(self.centralwidget)
        self.combo_from_city.setGeometry(QtCore.QRect(60, 80, 211, 22))
        self.combo_from_city.setObjectName("combo_from_city")
        self.combo_to_city = QtWidgets.QComboBox(self.centralwidget)
        self.combo_to_city.setGeometry(QtCore.QRect(390, 80, 211, 22))
        self.combo_to_city.setObjectName("combo_to_city")

        cities = pd.read_csv('cities.csv')
        for city in cities['municipality']:
            self.combo_from_city.addItem(city)
            self.combo_to_city.addItem(city)
        self.combo_from_city.setCurrentIndex(self.combo_from_city.findText("Wrocław"))
        self.combo_to_city.setCurrentIndex(self.combo_to_city.findText("London"))        
        
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setGeometry(QtCore.QRect(280, 430, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_search.setFont(font)
        self.button_search.setObjectName("button_search")
        self.label_from_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_from_1.setGeometry(QtCore.QRect(150, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_from_1.setFont(font)
        self.label_from_1.setObjectName("label_from_1")
        self.label_to_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_to_1.setGeometry(QtCore.QRect(470, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_to_1.setFont(font)
        self.label_to_1.setObjectName("label_to_1")
        self.label_from_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_from_3.setGeometry(QtCore.QRect(130, 120, 71, 16))
        self.label_from_3.setObjectName("label_from_3")
        self.label_to_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_to_3.setGeometry(QtCore.QRect(460, 120, 71, 16))
        self.label_to_3.setObjectName("label_to_3")
        self.calendar_from = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_from.setGeometry(QtCore.QRect(20, 140, 291, 181))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.calendar_from.setFont(font)
        self.calendar_from.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar_from.setNavigationBarVisible(True)
        self.calendar_from.setDateEditEnabled(True)
        self.calendar_from.setObjectName("calendar_from")
        self.calendar_to = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_to.setGeometry(QtCore.QRect(350, 140, 291, 181))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.calendar_to.setFont(font)
        self.calendar_to.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar_to.setNavigationBarVisible(True)
        self.calendar_to.setDateEditEnabled(True)
        self.calendar_to.setObjectName("calendar_to")
        self.text_email = QtWidgets.QTextEdit(self.centralwidget)
        self.text_email.setGeometry(QtCore.QRect(210, 380, 231, 31))
        self.text_email.setObjectName("text_email")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(290, 350, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.label_from_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_from_2.setGeometry(QtCore.QRect(60, 60, 81, 16))
        self.label_from_2.setObjectName("label_from_2")
        self.label_to_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_to_2.setGeometry(QtCore.QRect(390, 60, 81, 16))
        self.label_to_2.setObjectName("label_to_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.button_search.clicked.connect(self.click_search)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flight Scanner 1.0"))
        self.button_search.setText(_translate("MainWindow", "Szukaj"))
        self.label_from_1.setText(_translate("MainWindow", "Lot Z"))
        self.label_to_1.setText(_translate("MainWindow", "Lot Do"))
        self.label_from_3.setText(_translate("MainWindow", "Data Wylotu"))
        self.label_to_3.setText(_translate("MainWindow", "Data Wylotu"))
        self.label_email.setText(_translate("MainWindow", "Adres E-mail"))
        self.label_from_2.setText(_translate("MainWindow", "Nazwa miasta"))
        self.label_to_2.setText(_translate("MainWindow", "Nazwa miasta"))

    def get_date_from(self):
        return self.calendar_from.selectedDate().toPyDate()
        
    def get_date_to(self):
        return self.calendar_to.selectedDate().toPyDate()
         
    def get_city_from(self):
        return self.combo_from_city.currentText()

    def get_city_to(self):
        return self.combo_to_city.currentText()

    def get_email(self):
        return self.text_email.toPlainText()

    def click_search(self):
        date_from = self.get_date_from()
        date_to = self.get_date_to()
        
        city_from = self.get_city_from()
        city_to = self.get_city_to()

        email = self.get_email()

        if (date_from<date.today() or date_to<date.today()):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwa data")
            msg.setText("Wprowadzona data nie może być przeszła")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("Data wylotu: " + str(date_from) + "\n" + "Data powrotu: " + str(date_to))
            x = msg.exec_()
        elif (date_from>=date_to):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwa data")
            msg.setText("Data powrotu musi być większa niż data wylotu")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("Data wylotu: " + str(date_from) + "\n" + "Data powrotu: " + str(date_to))
            x = msg.exec_()
        elif (city_from == city_to):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwa miasto")
            msg.setText("Miasto powrotu musi być różne od miasta wylotu")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("Miasto wylotu: " + str(city_from) + "\n" + "Miasto powrotu: " + str(city_to))
            x = msg.exec_()
        elif (email == ""):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwa email")
            msg.setText("Pole Adres E-mail nie może być puste")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            print(date_from)
            print(date_to)
            print(city_from)
            print(city_to)
            print(email)
            search_button(city_from, city_to, date_from, date_to)
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
