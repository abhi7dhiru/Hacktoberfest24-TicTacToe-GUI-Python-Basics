from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi('Tic_Tac_Toe_UI.ui', self)

        # Adding the widgets to the file
        self.pushButton_1 = self.findChild(QPushButton, 'pushButton')
        self.pushButton_2 = self.findChild(QPushButton, 'pushButton_2')
        self.pushButton_3 = self.findChild(QPushButton, 'pushButton_3')
        self.pushButton_4 = self.findChild(QPushButton, 'pushButton_4')
        self.pushButton_5 = self.findChild(QPushButton, 'pushButton_5')
        self.pushButton_6 = self.findChild(QPushButton, 'pushButton_6')
        self.pushButton_7 = self.findChild(QPushButton, 'pushButton_7')
        self.pushButton_8 = self.findChild(QPushButton, 'pushButton_8')
        self.pushButton_9 = self.findChild(QPushButton, 'pushButton_9')
        self.label = self.findChild(QLabel, 'label')
        self.newGameButton = self.findChild(QPushButton, 'pushButton_10')

        # Connecting the buttons
        self.pushButton_1.clicked.connect(lambda: self.PushingButton(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.PushingButton(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.PushingButton(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.PushingButton(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.PushingButton(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.PushingButton(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.PushingButton(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.PushingButton(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.PushingButton(self.pushButton_9))
        self.newGameButton.clicked.connect(self.NewGame)

        
        self.show()

    # New Game clears the whole Board
    def NewGame(self):
        pass

    # Check button checks if X's is winning or O's is winning
    def Check(self):
        pass

    # Reaction when you push Buttons
    def PushingButton(self, btn):
        pass

app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()
