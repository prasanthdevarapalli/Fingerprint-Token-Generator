# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allinone.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMessageBox

import datetime

import os
import pandas as pd
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import example_delete as ed

Password='56789'




class Ui_AllInOne(object):
    def delnam(self):
        self.clear()
        self.name.setVisible(True)
        self.roll.setVisible(True)
        self.pasoutyr.setVisible(True)
        self.nameEdit_2.setVisible(True)
        self.rolledit.setVisible(True)
        self.yearedit.setVisible(True)
        self.pushButton_5.setVisible(True)

    def delname(self):
        df=pd.read_csv('hostel.csv')
        roll=self.nameEdit_2.text()
        val=df.query('Rollnum not in @roll')
        val.to_csv('hostel.csv',encoding="utf-8",index=False)
        ed.dele1(param)
        print("deleted")

    def anlys(self):
            self.clear()
            self.pushButton_7.setVisible(True)
##            self.pushButton_8.setVisible(True)
##            self.pushButton_9.setVisible(True)
            self.pushButton_10.setVisible(True)
            self.fromedit.setVisible(True)
            self.from1edit.setVisible(True)
            
    def printmsg(self):
        df=pd.read_csv('templunch8.csv')
        x=df.shape[0]
        print(x)
        os.system('\necho '+str(x)+' | lpr')
        df=pd.read_csv('templunch8.csv')
        x=df.shape[0]
        print(x)
        os.system('echo "Lunch"'+str(x)+' | lpr')
        df=pd.read_csv('templunch8.csv')
        x=df.shape[0]
        print(x)
        os.system('echo "Lunch"'+str(x)+' | lpr')
        
        
        
    def clear(self):
        
        
        self.pushButton_7.setVisible(False)
##        self.pushButton_8.setVisible(False)
##        self.pushButton_9.setVisible(False)
        self.pushButton_10.setVisible(False)

        self.name.setVisible(False)
        self.roll.setVisible(False)
        self.pasoutyr.setVisible(False)
        self.nameEdit_2.setVisible(False)
        self.rolledit.setVisible(False)
        self.yearedit.setVisible(False)
        self.pushButton.setVisible(False)

        self.name.setVisible(False)
        self.roll.setVisible(False)
        self.pasoutyr.setVisible(False)
        self.nameEdit_2.setVisible(False)
        self.rolledit.setVisible(False)
        self.yearedit.setVisible(False)
        self.pushButton_5.setVisible(False)
           
    def msg(self):
        
        self.password.setVisible(False)
        self.passedit.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.add.setVisible(False)
        self.delete_2.setVisible(False)
        self.name.setVisible(False)
        self.roll.setVisible(False)
        self.pasoutyr.setVisible(False)
        self.nameEdit_2.setVisible(False)
        self.rolledit.setVisible(False)
        self.yearedit.setVisible(False)
        self.pushButton.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(False)
        self.impo()
        
    def impo(self):
        
        import example_search
        place=self.place.setVisible(True)
        os._exit(1)

    def check(self):
        self.place.setVisible(False)
        self.password.setVisible(True)
        self.passedit.setVisible(True)
        self.pushButton_3.setVisible(True)
    
    def success(self):
        pas=self.passedit.text()
        if(pas==Password):
            self.add.setVisible(True)
            self.delete_2.setVisible(True)
            self.pushButton_4.setVisible(True)
            self.pushButton_6.setVisible(True)         
            self.pushButton_7.setVisible(False)

        else:
            print('wrong password')
            wrong = QtWidgets.QErrorMessage()
            wrong.showMessage('wrong password!')
            wrong.show(True)
            
        def do(self):
            import sys
            app = QtWidgets.QApplication(sys.argv)
            AllInOne = QtWidgets.QMainWindow()
            ui = Ui_AllInOne()
            ui.setupUi(AllInOne)
            AllInOne.show()
            sys.exit(app.exec_())
            
##    def analyas(self):
##        self.pushButton_8.setVisible(True)
        
        
            
            
    def addcheck(self):
        self.clear()  
        self.name.setVisible(True)
        self.roll.setVisible(True)
        self.pasoutyr.setVisible(True)
        self.nameEdit_2.setVisible(True)
        self.rolledit.setVisible(True)
        self.yearedit.setVisible(True)
        self.pushButton.setVisible(True)

    def added(self):
        print('success')
        try:
            f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

        ## Gets some sensor information
        print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

        ## Tries to enroll new finger
        try:
            print('Waiting for finger...')

            ## Wait that finger is read
            while ( f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            f.convertImage(0x01)

            ## Checks if finger is already enrolled
            result = f.searchTemplate()
            positionNumber = result[0]

            if ( positionNumber >= 0 ):
                print('Template already exists at position #' + str(positionNumber))

            print('Remove finger...')
            time.sleep(2)

            print('Waiting for same finger again...')

            ## Wait that finger is read again
            while ( f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 2
            f.convertImage(0x02)

            ## Compares the charbuffers
            if ( f.compareCharacteristics() == 0 ):
                raise Exception('Fingers do not match')

            ## Creates a template
            f.createTemplate()

            ## Saves template at new position number
            positionNumber = f.storeTemplate()
            print('Finger enrolled successfully!')
            print('New template position #' + str(positionNumber))
            df=pd.read_csv('hostel.csv')
            roll=self.nameEdit_2.text()
            yop=self.yearedit.text()
            x=df.shape[0]
            df.set_value(x,'Rollnum',roll)
            df.set_value(x,'fingerid',positionNumber)
            df.set_value(x,'YoP',yop)
            df.to_csv('hostel.csv',encoding="utf-8",index=False)
            print('success')
            

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))

        self.setupUi(AllInOne)
        
            
        
    def setupUi(self, AllInOne):
        AllInOne.setObjectName("AllInOne")
        AllInOne.resize(772, 516)

        self.title = 'PyQt5 messagebox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
         
        self.centralWidget = QtWidgets.QWidget(AllInOne)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 751, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sp.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.place = QtWidgets.QLabel(self.centralWidget)
        self.place.setGeometry(QtCore.QRect(260, 70, 301, 31))
        self.place1 = QtWidgets.QLabel(self.centralWidget)
        self.place1.setGeometry(QtCore.QRect(260, 70, 301, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.place.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.place.setFont(font)
        self.place.setObjectName("place")
        self.place.setVisible(False)
        self.place1.setFont(font)
        self.place1.setObjectName("place1")
        self.place1.setVisible(False)
        self.admin = QtWidgets.QPushButton(self.centralWidget)
        self.admin.setGeometry(QtCore.QRect(30, 40, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.admin.setFont(font)
        self.admin.setObjectName("admin")
        self.admin.clicked.connect(self.check)
        self.student = QtWidgets.QPushButton(self.centralWidget)
        self.student.setGeometry(QtCore.QRect(140, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.student.setFont(font)
        self.student.setObjectName("student")
        self.student.clicked.connect(self.msg)
        self.passedit = QtWidgets.QLineEdit(self.centralWidget)
        self.passedit.setGeometry(QtCore.QRect(60, 250, 151, 31))
        self.passedit.setObjectName("passedit")
        self.passedit.setVisible(False)
        self.password = QtWidgets.QLabel(self.centralWidget)
        self.password.setGeometry(QtCore.QRect(60, 200, 111, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.password.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.password.setVisible(False)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 320, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.success)
        self.pushButton_3.setVisible(False)
        self.add = QtWidgets.QPushButton(self.centralWidget)
        self.add.setGeometry(QtCore.QRect(610, 40, 75, 23))
        self.add.setObjectName("add")
        self.add.clicked.connect(self.addcheck)
        self.add.setVisible(False)
##        for i in range(3):
##            self.do()
        self.delete_2 = QtWidgets.QPushButton(self.centralWidget)
        self.delete_2.setGeometry(QtCore.QRect(610, 90, 75, 23))
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.delnam)
        self.delete_2.setVisible(False)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(530,130,75,23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setVisible(False)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(670,130,75,23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.anlys)
        self.pushButton_6.setVisible(False)
##        self.pushButton_6.clicked.connect(self.anlys)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(610,200,75,23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.printmsg)
        self.pushButton_7.setVisible(False)

        self.fromedit = QtWidgets.QPushButton(self.centralWidget)
        self.fromedit.setGeometry(QtCore.QRect(630,270,75,23))
        self.fromedit.setObjectName("fromedit")
        self.fromedit.setVisible(False)

        self.from1edit = QtWidgets.QLineEdit(self.centralWidget)
        self.from1edit.setGeometry(QtCore.QRect(60, 250, 151, 31))
        self.from1edit.setObjectName("from1edit")
        self.from1edit.setVisible(False)

##        self.fromedit = QtWidgets.QLabel(self.centralWidget)
##        self.fromedit.setGeometry(QtCore.QRect(610, 220, 301, 31))
##        font = QtGui.QFont()
##        font.setPointSize(20)
##        self.fromedit.setFont(font)
##        self.fromedit.setObjectName("fromedit")
##        self.fromedit.setVisible(False)
        
       
##        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
##        self.pushButton_8.setGeometry(QtCore.QRect(610,240,75,23))
##        self.pushButton_8.setObjectName("pushButton_8")
##        self.pushButton_8.setVisible(False)
##        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
##        self.pushButton_9.setGeometry(QtCore.QRect(610,280,75,23))
##        self.pushButton_9.setObjectName("pushButton_9")
##        self.pushButton_9.setVisible(False)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_10.setGeometry(QtCore.QRect(610,320,75,23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setVisible(False)        
        self.nameEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.nameEdit_2.setGeometry(QtCore.QRect(560, 180, 181, 21))
        self.nameEdit_2.setObjectName("nameEdit_2")
        self.nameEdit_2.setVisible(False)
        self.name = QtWidgets.QLabel(self.centralWidget)
        self.name.setGeometry(QtCore.QRect(540, 150, 71, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.name.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.name.setVisible(False)
        self.rolledit = QtWidgets.QLineEdit(self.centralWidget)
        self.rolledit.setGeometry(QtCore.QRect(560, 240, 181, 21))
        self.rolledit.setObjectName("rolledit")
        self.rolledit.setVisible(False)
        self.roll = QtWidgets.QLabel(self.centralWidget)
        self.roll.setGeometry(QtCore.QRect(540, 210, 71, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.roll.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.roll.setFont(font)
        self.roll.setObjectName("roll")
        self.roll.setVisible(False)
        self.yearedit = QtWidgets.QLineEdit(self.centralWidget)
        self.yearedit.setGeometry(QtCore.QRect(560, 300, 181, 21))
        self.yearedit.setObjectName("yearedit")
        self.yearedit.setVisible(False)
        self.pasoutyr = QtWidgets.QLabel(self.centralWidget)
        self.pasoutyr.setGeometry(QtCore.QRect(540, 270, 121, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pasoutyr.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pasoutyr.setFont(font)
        self.pasoutyr.setObjectName("pasoutyr")
        self.pasoutyr.setVisible(False)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setVisible(False)
        self.pushButton.clicked.connect(self.added)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 370, 100, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setVisible(False)
        
        self.pushButton_5.clicked.connect(self.delname)
##       self.pushButton_8.setGeometry(QtCore.QRect(600, 150, 75, 23))
##        self.pushButton_8.setObjectName("pushButton_8")
##        self.pushButton_8.setVisible(False)
        AllInOne.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(AllInOne)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menuBar.setObjectName("menuBar")
        AllInOne.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(AllInOne)
        self.mainToolBar.setObjectName("mainToolBar")
        AllInOne.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(AllInOne)
        self.statusBar.setObjectName("statusBar")
        AllInOne.setStatusBar(self.statusBar)

        self.retranslateUi(AllInOne)
        QtCore.QMetaObject.connectSlotsByName(AllInOne)
####        import sys
##        if(self.pushButton.clicked.connect):
##            app = QtWidgets.QApplication(sys.argv)
##            AllInOne = QtWidgets.QMainWindow()
##            ui = Ui_AllInOne()
##            ui.setupUi(AllInOne)
##            AllInOne.show()
####      sys.exit(app.exec_())
##            app.exec_()

    def retranslateUi(self, AllInOne):
        _translate = QtCore.QCoreApplication.translate
        AllInOne.setWindowTitle(_translate("AllInOne", "AllInOne"))
        self.place.setText(_translate("AllInOne", "Please place your finger"))
        self.place1.setText(_translate("AllInOne", "take your token"))
        self.admin.setText(_translate("AllInOne", "Admin"))
        self.student.setText(_translate("AllInOne", "Student"))
        self.password.setText(_translate("AllInOne", "Password :"))
        self.pushButton_3.setText(_translate("AllInOne", "login"))
        self.add.setText(_translate("AllInOne", "add"))
        self.delete_2.setText(_translate("AllInOne", "delete"))
        self.name.setText(_translate("AllInOne", "name :"))
        self.roll.setText(_translate("AllInOne", "roll no :"))
        self.pasoutyr.setText(_translate("AllInOne", "pass out year"))
        self.pushButton.setText(_translate("AllInOne", "Confirm"))
        self.pushButton_4.setText(_translate("AllInOne", "list"))
        self.pushButton_5.setText(_translate("AllInOne", "delete name"))
        
        self.pushButton_6.setText(_translate("AllInOne", "Analysis"))
        self.pushButton_7.setText(_translate("ALLInOne", "Today"))
        self.fromedit.setText(_translate("AllInOne", "From"))
##        self.fromedit.setText(_translate("AllInOne", "From date"))
##        self.pushButton_8.setText(_translate("AllInOne", "Week"))
##        self.pushButton_9.setText(_translate("AllInOne", "Month"))
        self.pushButton_10.setText(_translate("AllInOne", "count"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AllInOne = QtWidgets.QMainWindow()
    ui = Ui_AllInOne()
    ui.setupUi(AllInOne)
    AllInOne.show()
##    sys.exit(app.exec_())
    app.exec_()

