import sys
from PyQt5 import QtWidgets
import second
import threading
import random

class ExampleApp(QtWidgets.QMainWindow, second.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
window = ExampleApp()
isClose = False

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def rundomColor():
    if isClose == False:
        threading.Timer(10.0, rundomColor).start()
    else:
        return

    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    window.setStyleSheet("QMainWindow {background: '" + color + "';}");

def main():
    window.showFullScreen()
    rundomColor()
    app.exec_()
    global isClose
    isClose = True

if __name__ == '__main__':
    main()
