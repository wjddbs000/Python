import sys
from PyQt5.QWidgets import QMessageBox, QMenuBar, QApplication, QWidget, QAction, QMainWindow, QPushButton
# from PyQt5.QWidgets import QMessageBox, QMenuBar, QApplication, QWidget, QAction, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QCoreApplication 

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('logout.png'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.btn_clicked)

        menubar=self.menubar()
        #menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        button = QPushButton('Quit',self)
        button.move(50,50)
        button.resize(button.sizeHint())
        button.clicked.connect(self.btn_clicked)

        self.setWindowTitle('My Qt App')
        self.setWindowIcon(QIcon('box.png'))
        self.setGeometry(100,100,640,400)
        self.show()

    def btn_clicked(self):
        sys.exit(0)
        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())