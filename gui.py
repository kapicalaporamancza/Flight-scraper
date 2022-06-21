from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
from kayak_f import search_button

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 690)
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
        self.button_search.setGeometry(QtCore.QRect(280, 600, 101, 28))
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
        self.text_email.setGeometry(QtCore.QRect(210, 550, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.text_email.setFont(font)
        self.text_email.setObjectName("text_email")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(290, 520, 81, 16))
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
        self.label_parameters = QtWidgets.QLabel(self.centralwidget)
        self.label_parameters.setGeometry(QtCore.QRect(250, 430, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_parameters.setFont(font)
        self.label_parameters.setObjectName("label_parameters")
        self.combo_cooldown = QtWidgets.QComboBox(self.centralwidget)
        self.combo_cooldown.setGeometry(QtCore.QRect(150, 480, 121, 22))
        self.combo_cooldown.setObjectName("combo_cooldown")
        self.combo_amount = QtWidgets.QComboBox(self.centralwidget)
        self.combo_amount.setGeometry(QtCore.QRect(382, 480, 121, 22))
        self.combo_amount.setObjectName("combo_amount")

        for x in range(30):
            self.combo_amount.addItem(str(x+1))
        self.combo_amount.setCurrentIndex(self.combo_amount.findText("1"))
        self.combo_cooldown.addItem("12 godzin")
        self.combo_cooldown.addItem("24 godziny")
        self.combo_cooldown.addItem("48 godzin")
        self.combo_cooldown.addItem("1 minuta")
        self.combo_cooldown.setCurrentIndex(self.combo_cooldown.findText("24 godziny"))        

        self.label_cooldown = QtWidgets.QLabel(self.centralwidget)
        self.label_cooldown.setGeometry(QtCore.QRect(150, 460, 161, 16))
        self.label_cooldown.setObjectName("label_cooldown")
        self.label_amount = QtWidgets.QLabel(self.centralwidget)
        self.label_amount.setGeometry(QtCore.QRect(380, 460, 161, 16))
        self.label_amount.setObjectName("label_amount")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 340, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 370, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 370, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 370, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 370, 55, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_adults = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_adults.setGeometry(QtCore.QRect(150, 390, 73, 22))
        self.comboBox_adults.setObjectName("comboBox_adults")
        self.comboBox_students = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_students.setGeometry(QtCore.QRect(240, 390, 73, 22))
        self.comboBox_students.setObjectName("comboBox_students")
        self.comboBox_teenagers = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_teenagers.setGeometry(QtCore.QRect(340, 390, 73, 22))
        self.comboBox_teenagers.setObjectName("comboBox_teenagers")
        self.comboBox_children = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_children.setGeometry(QtCore.QRect(430, 390, 73, 22))
        self.comboBox_children.setObjectName("comboBox_children")

        for x in range(10):
            self.comboBox_adults.addItem(str(x))
            self.comboBox_students.addItem(str(x))

        for x in range(8):
            self.comboBox_teenagers.addItem(str(x))
            self.comboBox_children.addItem(str(x))

        self.comboBox_adults.setCurrentIndex(self.comboBox_adults.findText("1"))
        self.comboBox_students.setCurrentIndex(self.comboBox_students.findText("0"))       
        self.comboBox_teenagers.setCurrentIndex(self.comboBox_teenagers.findText("0"))       
        self.comboBox_children.setCurrentIndex(self.comboBox_children.findText("0"))               


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
        self.label_parameters.setText(_translate("MainWindow", "Parametry wyszukiwań"))
        self.label_cooldown.setText(_translate("MainWindow", "Częstotliwość wyszukiwania"))
        self.label_amount.setText(_translate("MainWindow", "Ilość wyszukiwań"))
        self.label.setText(_translate("MainWindow", "Ilość poszczególnych biletów"))
        self.label_2.setText(_translate("MainWindow", "Dorośli"))
        self.label_3.setText(_translate("MainWindow", "Studenci"))
        self.label_4.setText(_translate("MainWindow", "Nastolatki"))
        self.label_5.setText(_translate("MainWindow", "Dzieci"))

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

    def get_amount(self):
        return self.combo_amount.currentText()
    
    def get_cooldown(self):
        return self.combo_cooldown.currentText()

    def get_adults(self):
        return self.comboBox_adults.currentText()

    def get_students(self):
        return self.comboBox_students.currentText()

    def get_teenagers(self):
        return self.comboBox_teenagers.currentText()

    def get_children(self):
        return self.comboBox_children.currentText()

    def click_search(self):
        date_from = self.get_date_from()
        date_to = self.get_date_to()
        
        city_from = self.get_city_from()
        city_to = self.get_city_to()

        email = self.get_email()
        amount = int(self.get_amount())
        cooldown = self.get_cooldown()

        adults = int(self.get_adults())
        students = int(self.get_students())
        teenagers = int(self.get_teenagers())
        children = int(self.get_children())

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
            msg.setWindowTitle("Niewłaściwe miasto")
            msg.setText("Miasto powrotu musi być różne od miasta wylotu")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("Miasto wylotu: " + str(city_from) + "\n" + "Miasto powrotu: " + str(city_to))
            x = msg.exec_()
        elif (email == ""):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwy email")
            msg.setText("Pole Adres E-mail nie może być puste")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif (adults==0 and students==0 and teenagers==0 and children==0):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwa ilość biletów")
            msg.setText("Musisz wybrać co najmnniej jeden bilet")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        elif (adults==0 and students==0):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwa ilość biletów")
            msg.setText("Aplikacja nie obsługuje wyszukiwań dla osób małoletnich bez opieki. Musisz wybrać co najmnniej jeden bilet dla dorosłego lub studenta")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()            
        elif (adults+students>9):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwa ilość biletów")
            msg.setText("Suma biletów dla dorosłych oraz studentów nie może być większa niż 9")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("Liczba biletów dla dorosłych: " + str(adults) + "\n" + "Liczba biletów dla studentów: " + str(students))            
            x = msg.exec_()  
        elif (teenagers+children>7):
            msg = QMessageBox()
            msg.setWindowTitle("Niewłaściwa ilość biletów")
            msg.setText("Suma biletów dla nastolatków oraz dzieci nie może być większa niż 7")
            msg.setIcon(QMessageBox.Warning)
            msg.setDetailedText("Liczba biletów dla nastolatków: " + str(teenagers) + "\n" + "Liczba biletów dla dzieci: " + str(children))            
            x = msg.exec_()                
        else:
            search_button(city_from, city_to, date_from, date_to, email, cooldown, amount, adults, students, teenagers, children)
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())