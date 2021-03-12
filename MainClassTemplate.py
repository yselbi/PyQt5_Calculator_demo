
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(381, 625)
        self.main_surface = QtWidgets.QFrame(Form)
        self.main_surface.setGeometry(QtCore.QRect(10, 10, 361, 611))
        self.main_surface.setStyleSheet("#main_surface{\n"
"\n"
"    background-image: url(bg/skin.png);\n"
"\n"
"}\n"
"\n"
"\n"
"#pushButton_close{\n"
"\n"
"    background-color: rgb(255, 170, 0);\n"
"    \n"
"   border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"#pushButton_close:pressed{\n"
"\n"
"border: 3px solid rgb(255, 225, 194);\n"
"}\n"
"\n"
"\n"
"#pushButton_clear, #pushButton_div,#pushButton_sub,#pushButton_mul,#pushButton_results,#pushButton_point,\n"
"#pushButton_0,#pushButton_1,#pushButton_2,#pushButton_3,#pushButton_4,#pushButton_5,#pushButton_6,\n"
"#pushButton_7,#pushButton_8,#pushButton_9 {\n"
"\n"
"    background-color: rgba(221, 221, 221,50);\n"
"\n"
"   border-top-left-radius: 8px;\n"
"  border-top-right-radius: 8px;\n"
"\n"
"   border-bottom-left-radius:15px;\n"
"  border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"#pushButton_clear:pressed, #pushButton_div:pressed,#pushButton_sub:pressed,#pushButton_mul:pressed,#pushButton_results:pressed,#pushButton_point:pressed,\n"
"#pushButton_0:pressed,#pushButton_1:pressed,#pushButton_2:pressed,#pushButton_3:pressed,#pushButton_4:pressed,#pushButton_5:pressed,#pushButton_6:pressed,\n"
"#pushButton_7:pressed,#pushButton_8:pressed,#pushButton_9:pressed{\n"
"\n"
"border: 3px solid rgb(238, 238, 238);\n"
"}\n"
"\n"
"\n"
"\n"
"#pushButton_add{\n"
"\n"
"    background-color: rgba(221, 221, 221,50);\n"
"   border-radius:8px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#pushButton_add:pressed{\n"
"\n"
"    border: 3px solid rgb(238, 238, 238);\n"
"\n"
"}")
        self.main_surface.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_surface.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_surface.setObjectName("main_surface")
        self.pushButton_3 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_3.setGeometry(QtCore.QRect(192, 465, 61, 51))
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_clear = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_clear.setGeometry(QtCore.QRect(191, 242, 61, 51))
        self.pushButton_clear.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("")
        self.pushButton_clear.setText("")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_4 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_4.setGeometry(QtCore.QRect(31, 391, 61, 51))
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_mul = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_mul.setGeometry(QtCore.QRect(273, 317, 61, 51))
        self.pushButton_mul.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_mul.setStyleSheet("")
        self.pushButton_mul.setText("")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_9 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_9.setGeometry(QtCore.QRect(192, 317, 61, 51))
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_results = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_results.setGeometry(QtCore.QRect(193, 539, 61, 51))
        self.pushButton_results.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_results.setStyleSheet("")
        self.pushButton_results.setText("")
        self.pushButton_results.setObjectName("pushButton_results")
        self.pushButton_1 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_1.setGeometry(QtCore.QRect(31, 465, 61, 51))
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_1.setStyleSheet("")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_5 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_5.setGeometry(QtCore.QRect(112, 391, 61, 51))
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_close = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_close.setGeometry(QtCore.QRect(182, 24, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_add = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_add.setGeometry(QtCore.QRect(272, 461, 61, 131))
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_add.setStyleSheet("")
        self.pushButton_add.setText("")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_sub = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_sub.setGeometry(QtCore.QRect(272, 390, 61, 51))
        self.pushButton_sub.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_sub.setStyleSheet("")
        self.pushButton_sub.setText("")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_7 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_7.setGeometry(QtCore.QRect(31, 318, 61, 51))
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_point = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_point.setGeometry(QtCore.QRect(112, 539, 61, 51))
        self.pushButton_point.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_point.setStyleSheet("")
        self.pushButton_point.setText("")
        self.pushButton_point.setObjectName("pushButton_point")
        self.pushButton_6 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_6.setGeometry(QtCore.QRect(192, 391, 61, 51))
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_8.setGeometry(QtCore.QRect(111, 318, 61, 51))
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_0 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_0.setGeometry(QtCore.QRect(32, 540, 61, 51))
        self.pushButton_0.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_0.setStyleSheet("")
        self.pushButton_0.setText("")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_div = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_div.setGeometry(QtCore.QRect(272, 241, 61, 51))
        self.pushButton_div.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_div.setStyleSheet("")
        self.pushButton_div.setText("")
        self.pushButton_div.setObjectName("pushButton_div")
        self.lcdNumber = QtWidgets.QLCDNumber(self.main_surface)
        self.lcdNumber.setGeometry(QtCore.QRect(31, 106, 301, 101))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_2 = QtWidgets.QPushButton(self.main_surface)
        self.pushButton_2.setGeometry(QtCore.QRect(112, 465, 61, 51))
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_close.setText(_translate("Form", "Close "))
