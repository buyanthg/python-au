import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow


class Calculator(QMainWindow):
    res = 0
    oper = ''
    fNewNum = 1

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.but_0.clicked.connect(lambda: self.add_dight('0'))
        self.ui.but_1.clicked.connect(lambda: self.add_dight('1'))
        self.ui.but_2.clicked.connect(lambda: self.add_dight('2'))
        self.ui.but_3.clicked.connect(lambda: self.add_dight('3'))
        self.ui.but_4.clicked.connect(lambda: self.add_dight('4'))
        self.ui.but_5.clicked.connect(lambda: self.add_dight('5'))
        self.ui.but_6.clicked.connect(lambda: self.add_dight('6'))
        self.ui.but_7.clicked.connect(lambda: self.add_dight('7'))
        self.ui.but_8.clicked.connect(lambda: self.add_dight('8'))
        self.ui.but_9.clicked.connect(lambda: self.add_dight('9'))
        self.ui.but_del.clicked.connect(lambda: self.del_num())
        self.ui.but_clr.clicked.connect(lambda: self.clear())
        self.ui.but_pls.clicked.connect(lambda: self.operation('+'))
        self.ui.but_mns.clicked.connect(lambda: self.operation('-'))
        self.ui.but_mul.clicked.connect(lambda: self.operation('*'))
        self.ui.but_div.clicked.connect(lambda: self.operation('/'))
        self.ui.but_eq.clicked.connect(lambda: self.result())

    def add_dight(self, btn_txt):
        if self.fNewNum == 1:
            self.ui.line.setText(btn_txt)
            self.fNewNum = 0
        else:
            self.ui.line.setText(self.ui.line.text() + btn_txt)

    def result(self):
        if self.oper != '':
            if self.fNewNum == 0:
                self.operation('')
            self.ui.line.setText(str(self.res))
            self.ui.label.setText('')
        self.res = 0
        self.oper = ''
        self.fNewNum = 1

    def del_num(self):
        if len(self.ui.label.text()) == 1:
            self.ui.line.setText('0')
            self.fNewNum = 1
        elif self.ui.line.text() != '0':
            self.ui.line.setText(self.ui.label.text()[:-1])

    def clear(self):
        self.ui.label.setText('')
        self.ui.line.setText('0')
        self.fNewNum = 1
        self.res = 0
        self.oper = ''

    def operation(self, btn_txt):
        if not (btn_txt == '/' and self.res == 0) and self.ui.line.text() != '0':
            if self.oper == '':
                self.res = int(self.ui.line.text())
            else:
                if self.oper == '+':
                    self.res += int(self.ui.line.text())
                elif self.oper == '-':
                    self.res -= int(self.ui.line.text())
                elif self.oper == '*':
                    self.res *= int(self.ui.line.text())
                elif self.oper == '/':
                    self.res /= int(self.ui.line.text())

            self.ui.label.setText(str(self.res)+btn_txt)
            self.oper = btn_txt
            self.fNewNum = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
