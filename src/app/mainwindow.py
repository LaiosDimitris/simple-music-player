from PyQt5.QtWidgets import *
import threading


class MainWindow(QWidget):
    """
    Application's main window.

    """
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.__winTitle = 'Simple Music Player'
        self.__winWidth = 1200
        self.__winHeight = 700
        self.__setWindowSize()
        self.__setWindowTitle()
        self.__setWindowIcon()
        self.__initializeUI()

    def __setWindowSize(self):
        self.setFixedSize(self.__winWidth, self.__winHeight)

    def __setWindowTitle(self):
        self.setWindowTitle(self.__winTitle)

    #TODO
    def __setWindowIcon(self):
        pass

    def __initializeUI(self):
        self.__initializeGridLayout()

    def __initializeGridLayout(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

    
    

    