import sys
import subprocess
import pyautogui


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *

except ImportError:

    install('pyqt5')
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *


class Button:

    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results

        self.b.clicked.connect(lambda: self.handelInput(self.text))


    def handelInput(self, v):
        file1 = open("File.txt", "w+",encoding='utf8')

        print("clicked", v)
        if (self.text == "<-"):
            current_value = self.results.text()
            new_value = str(current_value[:-1])
        elif (self.text == "Erase"):
            new_value = ""
        elif (self.text=="Space"):
            current_value = self.results.text()
            new_value=str(current_value+" ")
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
        self.results.setText(new_value)
        file1.write(str(new_value))
        file1.close()


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DEVNAGRI INTERFACE ")
        self.CreateApp()

    def CreateApp(self):

        grid = QGridLayout()
        results = QLineEdit()

        buttons = ["<-", "Erase","Space","०","१","२","३","४","५","६","७","८","९",".","ॽ","|",",","!","अ","आ","इ","ई","उ","ऊ","ऋ","ए","ऎ","ऒ","औ","ॐ","क","ख",
                   "ग","घ","ङ","च","छ","ज","झ","ञ","ट","ठ","ड","ढ","ण","त","थ","द","ध","न","प","फ",
                   "ब","भ","म","य","र","ल","व","श","ष","स","ह","ळ","ा","ि","ी","ु",
                   "ू","ृ","े","ै","ो","ौ","्","ँ","ं","ः" ]
        grid.addWidget(results, 0, 0, 1, 12)
        row = 2
        col = 0
        for button in buttons:
            butobj = Button(button, results)
            if button=="०":
                col=9
                row=1
            elif col > 11 or  button == "अ" or button=="क" :
                col = 0
                row = row + 1


            print(row, " ", col, " ", button)
            if (button == "Erase"):
                grid.addWidget(butobj.b, 1, 3, 1, 3)
            elif (button == "<-"):
                grid.addWidget(butobj.b, 1, 0, 1, 3)
            elif(button=="Space"):
                grid.addWidget(butobj.b, 1, 6, 1, 3)
            else:
                grid.addWidget(butobj.b, row, col, 1, 1)
            col = col + 1

        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())

