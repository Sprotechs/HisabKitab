# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/addInvestor.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(140, 100, 241, 31))
        self.nameInput.setObjectName("nameInput")
        self.contactInput = QtWidgets.QLineEdit(self.centralwidget)
        self.contactInput.setGeometry(QtCore.QRect(140, 150, 241, 31))
        self.contactInput.setText("")
        self.contactInput.setObjectName("contactInput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 249, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.addressInput = QtWidgets.QLineEdit(self.centralwidget)
        self.addressInput.setGeometry(QtCore.QRect(140, 200, 241, 31))
        self.addressInput.setObjectName("addressInput")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(40, 319, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.joinDateInput = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.joinDateInput.setGeometry(QtCore.QRect(140, 250, 241, 31))
        self.joinDateInput.setDate(QtCore.QDate(2020, 1, 1))
        self.joinDateInput.setTime(QtCore.QTime(9, 0, 0))
        self.joinDateInput.setDisplayFormat("dd/MMMM/yyyy")
        self.joinDateInput.setObjectName("joinDateInput")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Investors"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Contact:"))
        self.label_3.setText(_translate("MainWindow", "Join Date:"))
        self.label_7.setText(_translate("MainWindow", "Address:"))
        self.label_4.setText(_translate("MainWindow", "Add Investor"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
