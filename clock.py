# -*- coding: utf-8 -*-
#Digital Clock Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#Digital Clock comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991

from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
import os, sys, time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()

#Update time.
    def update_time(self):
        real_time=time.strftime ("%H:%M")
        a=(real_time)
        self.lcd.display(a)
	
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(183, 90)
        Dialog.setMinimumSize(QtCore.QSize(183, 90))
        Dialog.setMaximumSize(QtCore.QSize(183, 90))
        Dialog.setStyleSheet(_fromUtf8("QDialog#Dialog{background-color:#686868;color:#1e580c;}"))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcd = QLCDNumber(Dialog)
        self.lcd.setStyleSheet(_fromUtf8("QLCDNumber#lcd{background-color:#353535;color:#9c9d65;}"))
        self.lcd.setObjectName(_fromUtf8("lcd"))
        self.verticalLayout.addWidget(self.lcd)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Digital_Clock", None))

#Timer to check time every n milliseconds.
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(100) #Update every 100 milliseconds.  

#Frameless Window.
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) #Frameless window declaration.

class Extra(Ui_Dialog):
#Creating a subclass for keyPressEvents and closeEvents. 
#They cannot be in the same class as the ui stuff. If
#they were they would fail to get triggered(launched).
#Notice that this class inherits directly from its parent and it does not have init and it does not have super declaration.

#Ignore ALT+F4. We want to avoid accidental closing.
    def closeEvent(self, event):
        event.ignore()

#Keypresses go below.    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.alts(event) #Esc key launches Quit program prompt.

#Exit/Quit program prompt. This catches Esc key.
    def alts(self, event):
        buttonReply = QMessageBox.question(self, 'Question', "Exit program?", QMessageBox.Cancel | QMessageBox.Ok  )
        
        if buttonReply == QMessageBox.Ok:
            print('Ok clicked, messagebox closed.')
            event.accept()
            app.quit()
            print "\n"
            print "Program ends. Goodbye."
            print "\n"    
        if buttonReply == QMessageBox.Cancel:
            print "Do not quit. --> Going back to the program."
            event.ignore() 

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = Extra()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
