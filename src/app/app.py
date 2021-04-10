from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

class App(QApplication):
    """
    Graphical interface using PyQt5.
    
    """
    def __init__(self, argv) -> None:
        super().__init__(argv)
        self.__mainWindow = MainWindow()

    def run(self):
        self.__mainWindow.show()
        sys.exit(self.exec_())

if __name__ == "__main__":
    app = App(sys.argv)
    app.run()

