
###################################################
#
#  project name :  Calculator Demo
#  version : 0.0.1
#  author : YAHYA SELBI
#  Last update : 12.03.2021
#  Note: I used eval function to handle calculator operations
#        project can be developed to add an extra features

##################################################



from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import sys


from MainClassTemplate import Ui_Form


class MainWindow(Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.stack = [""]
        self.is_ready = False
        self.results = ""
        self.decimal_point_counter = 0

        self.pushButton_close.clicked.connect(lambda: self.close())
        self.pushButton_point.clicked.connect(self.activate_decimal_point)

        self.pushButton_0.clicked.connect(lambda: self.input_numberS("0"))
        self.pushButton_1.clicked.connect(lambda: self.input_numberS("1"))
        self.pushButton_2.clicked.connect(lambda: self.input_numberS("2"))
        self.pushButton_3.clicked.connect(lambda: self.input_numberS("3"))
        self.pushButton_4.clicked.connect(lambda: self.input_numberS("4"))
        self.pushButton_5.clicked.connect(lambda: self.input_numberS("5"))
        self.pushButton_6.clicked.connect(lambda: self.input_numberS("6"))
        self.pushButton_7.clicked.connect(lambda: self.input_numberS("7"))
        self.pushButton_8.clicked.connect(lambda: self.input_numberS("8"))
        self.pushButton_9.clicked.connect(lambda: self.input_numberS("9"))
        self.pushButton_point.clicked.connect(lambda: self.input_numberS("."))


        self.pushButton_add.clicked.connect(lambda: self.get_operator("+"))
        self.pushButton_sub.clicked.connect(lambda: self.get_operator("-"))
        self.pushButton_mul.clicked.connect(lambda: self.get_operator("*"))
        self.pushButton_div.clicked.connect(lambda: self.get_operator("/"))

        self.pushButton_results.clicked.connect(self.show_results)

        self.pushButton_clear.clicked.connect(self.reset)


    def show_results(self):
        try :
            self.results = ""
            for each in self.stack:
                self.results += each

            self.lcdNumber.display(str(eval(self.results)))
        except:
            self.lcdNumber.display("ERR")

    def activate_decimal_point(self):
        self.decimal_point_counter +=1

    def input_numberS(self, num):

        if num != "0":
            self.is_ready = True

        if self.is_ready:
            if self.decimal_point_counter == 1 :
               self.stack[-1] += num
            elif num !=".":
                self.stack[-1] += num
            self.lcdNumber.display(self.stack[-1])

    def get_operator(self, op):
        self.stack.append(op)
        self.decimal_point_counter=0

    def reset(self):
        self.results = ""
        self.stack=[""]
        self.lcdNumber.display("0")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()

    sys.exit(app.exec_())