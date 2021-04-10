import tkinter as tk
import threading

class App(tk.Tk):
    """
    Graphical interface using Tkinter.
    
    """
    def __init__(self) -> None:
        super().__init__()
        self.__winWidth = 1200
        self.__winHeight = 700
        self.__windowInit()
        self.__uiInit()
        self.mainloop()

    def __windowInit(self):
        """
        Sets the window's dimensions, title and icon.
        
        """
        self.geometry(f"{self.__winWidth}x{self.__winHeight}")
        self.title('Simple Music Player')
        self.resizable(0, 0)

    def __uiInit(self):
        pass

App()