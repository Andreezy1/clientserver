import clientconnect
import json
import hashlib

import mainwin
import loginpass
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

#class okna login and pass
class loginpasswin(QtWidgets.QMainWindow, loginpass.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.checklogpas)#sobitie click

    #proverka logina and pass
    def checklogpas(self):
        #priem logina and pass
        logpas = []
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        hashpass = hashlib.md5(password.encode())#hash
        logpas.append(login)#zapis v spisok
        logpas.append(hashpass.hexdigest())

        logpas = json.dumps(logpas)#convert v json

        sock.send(logpas.encode('utf-8'))# otpravka

        otvet = sock.recv(1024)#priem otveta ot servera
        otvet = json.loads(otvet.decode("utf-8"))
        if otvet == 0:
            QtWidgets.QMessageBox.about(self, "Error", "Не правильный логин или пароль")
        else:
            self.window2 = mainwindow()
            self.window2.show()
            self.window().close()



class mainwindow(QtWidgets.QMainWindow, mainwin.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.vivodtabl)  # sobitie click
        self.pushButton_2.clicked.connect(self.dobavit) #dobavit stroku
        self.pushButton_3.clicked.connect(self.insertdannie) #peredacha dannih
        self.pushButton_4.clicked.connect(self.deletdannie)


    def vivodtabl(self):#vivod tablici
        comanda = 0
        name = self.lineEdit.text() #imya
        comname = [comanda,name]
        comname = json.dumps(comname)  # convert v json
        sock.send(comname.encode('utf-8'))  # otpravka
        otvet = sock.recv(1024)  # priem otveta ot servera
        otvet = json.loads(otvet.decode("utf-8"))

        labels = otvet[len(otvet)-1] #nazvaniya colonok
        labels1 = []
        otvet.pop()
        global kolstrok
        kolstrok = len(otvet)
        for i in range(len(labels)):
            for j in range(len(labels[i])):
               labels1.append(labels[i][j])
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(otvet))
        self.tableWidget.setColumnCount(len(otvet[0]))
        self.tableWidget.setHorizontalHeaderLabels(labels1)

        # zapis v tablicu
        row = 0
        for tup in otvet:
            col = 0
            for item in tup:
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(item)))
                col += 1
            row += 1

    #dobaclenie stroki dly vvoda
    def dobavit(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    #insert dannie v tablicu
    def insertdannie(self):
        dannieinsert = []
        comanda = 1
        name = self.lineEdit.text()  # imya
        for i in range(self.tableWidget.rowCount()):
            dannieinsert.append([])
            for j in range(self.tableWidget.columnCount()):
                dannieinsert[i].append(self.tableWidget.item(i, j).text())
        dannieinsertotp = dannieinsert[kolstrok:len(dannieinsert)]
        comname = [comanda, name, dannieinsertotp]
        comname = json.dumps(comname)  # convert v json
        sock.send(comname.encode('utf-8'))  # otpravka

    #udalenie ilimenta
    def deletdannie(self):
        delitem = self.tableWidget.selectedItems() #udalyaemaya stroka
        stolbec = self.tableWidget.horizontalHeaderItem(delitem[0].column()) # po stolbcu
        comanda = 2 #komanda
        name = self.lineEdit.text()  # imya tabl
        buttonReply = QtWidgets.QMessageBox.question(self, 'Удалить?', "Вы действительно хотите удалить " + delitem[0].text() + " ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            comdel = [comanda, name, delitem[0].text(), stolbec.text()]
            comdel = json.dumps(comdel)
            print(comdel)
            sock.send(comdel.encode('utf-8'))
            self.tableWidget.removeRow(delitem[0].row())


    def closeEvent(self, event):
        comanda = [3]
        sock.send(json.dumps(comanda).encode('utf-8'))


#funkciya zapuska oknf login pass
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = loginpasswin()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

#ustanovka svyazi
sock = clientconnect.serverconnect()
#vizof funkcii
main()



