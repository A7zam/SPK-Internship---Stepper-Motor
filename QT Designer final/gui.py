# Form implementation generated from reading ui file 'guiii.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 60, 121, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 340, 181, 16))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 161, 16))
        self.label_4.setObjectName("label_4")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 100, 89, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 180, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.dial = QtWidgets.QDial(parent=self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(450, 10, 281, 231))
        self.dial.setObjectName("dial")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 500, 75, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 49, 16))
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 230, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 400, 61, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 400, 21, 16))
        self.label_8.setObjectName("label_8")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(20, 490, 421, 41))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(150, 130, 89, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(150, 30, 89, 20))
        self.radioButton.setObjectName("radioButton")
        self.executeNcwpbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.executeNcwpbtn.setGeometry(QtCore.QRect(270, 280, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.executeNcwpbtn.setFont(font)
        self.executeNcwpbtn.setObjectName("executeNcwpbtn")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 440, 191, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.executeNccwpbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.executeNccwpbtn.setGeometry(QtCore.QRect(270, 330, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.executeNccwpbtn.setFont(font)
        self.executeNccwpbtn.setObjectName("executeNccwpbtn")
        self.CWlineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.CWlineEdit.setGeometry(QtCore.QRect(220, 290, 31, 21))
        self.CWlineEdit.setObjectName("CWlineEdit")
        self.CCWlineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.CCWlineEdit.setGeometry(QtCore.QRect(220, 340, 31, 21))
        self.CCWlineEdit.setObjectName("CCWlineEdit")
        self.stepDelayLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.stepDelayLineEdit.setGeometry(QtCore.QRect(110, 400, 31, 21))
        self.stepDelayLineEdit.setObjectName("stepDelayLineEdit")
        self.stepDelaypbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stepDelaypbtn.setGeometry(QtCore.QRect(180, 400, 75, 24))
        self.stepDelaypbtn.setObjectName("stepDelaypbtn")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.radioButton_2.setText(_translate("SecondWindow", "Counter clockwise"))
        self.label_6.setText(_translate("SecondWindow", "Send \'N\' Steps Counterclockwise"))
        self.label_3.setText(_translate("SecondWindow", "Single Step Clockwise"))
        self.label_4.setText(_translate("SecondWindow", "Single Step Counterclockwise"))
        self.radioButton_3.setText(_translate("SecondWindow", "Full Step"))
        self.pushButton_8.setText(_translate("SecondWindow", "Execute Single Step CW"))
        self.pushButton_4.setText(_translate("SecondWindow", "Execute CLI"))
        self.label_5.setText(_translate("SecondWindow", "Send \'N\' Steps Clockwise"))
        self.label_2.setText(_translate("SecondWindow", "Step Size"))
        self.label.setText(_translate("SecondWindow", "Rotation"))
        self.pushButton_7.setText(_translate("SecondWindow", "Execute Single Step CCW"))
        self.label_7.setText(_translate("SecondWindow", "Step Delay"))
        self.label_8.setText(_translate("SecondWindow", "ms"))
        self.radioButton_4.setText(_translate("SecondWindow", "Half Step"))
        self.radioButton.setText(_translate("SecondWindow", "Clockwise"))
        self.executeNcwpbtn.setText(_translate("SecondWindow", "Execute \'N\' CW"))
        self.pushButton_3.setText(_translate("SecondWindow", "Initialize Stepper Motor"))
        self.executeNccwpbtn.setText(_translate("SecondWindow", "Execute \'N\' CCW"))
        self.CWlineEdit.setText(_translate("SecondWindow", "000"))
        self.CCWlineEdit.setText(_translate("SecondWindow", "000"))
        self.stepDelayLineEdit.setText(_translate("SecondWindow", "000"))
        self.stepDelaypbtn.setText(_translate("SecondWindow", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec())
