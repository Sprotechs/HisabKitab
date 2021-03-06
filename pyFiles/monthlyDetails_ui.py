# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/monthlyDetails.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 100, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(110, 100, 181, 31))
        self.nameLabel.setText("")
        self.nameLabel.setObjectName("nameLabel")
        self.typeLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeLabel.setGeometry(QtCore.QRect(430, 90, 151, 31))
        self.typeLabel.setText("")
        self.typeLabel.setObjectName("typeLabel")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(110, 130, 181, 31))
        self.totalLabel.setText("")
        self.totalLabel.setObjectName("totalLabel")
        self.paidLabel = QtWidgets.QLabel(self.centralwidget)
        self.paidLabel.setGeometry(QtCore.QRect(30, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.paidLabel.setFont(font)
        self.paidLabel.setObjectName("paidLabel")
        self.remainLabel = QtWidgets.QLabel(self.centralwidget)
        self.remainLabel.setGeometry(QtCore.QRect(430, 130, 151, 31))
        self.remainLabel.setText("")
        self.remainLabel.setObjectName("remainLabel")
        self.balanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.balanceLabel.setGeometry(QtCore.QRect(340, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.balanceLabel.setFont(font)
        self.balanceLabel.setObjectName("balanceLabel")
        self.detailsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.detailsTable.setGeometry(QtCore.QRect(30, 190, 561, 401))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.detailsTable.setFont(font)
        self.detailsTable.setObjectName("detailsTable")
        self.detailsTable.setColumnCount(5)
        self.detailsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailsTable.setHorizontalHeaderItem(4, item)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(635, 31, 321, 561))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Monthly Details"))
        self.label_4.setText(_translate("MainWindow", "Monthly Details"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Type:"))
        self.paidLabel.setText(_translate("MainWindow", "Total Paid:"))
        self.balanceLabel.setText(_translate("MainWindow", "Remaining:"))
        item = self.detailsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Year"))
        item = self.detailsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Month"))
        item = self.detailsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount Paid"))
        item = self.detailsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cost"))
        item = self.detailsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Profit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
