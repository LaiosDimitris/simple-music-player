from tkinter import ttk
import tkinter as tk
import threading

class Mainwindow(tk.Tk):
    """
    Graphical interface using Tkinter.
    
    """
    def __init__(self) -> None:
        super().__init__()
        self.__winTitle = 'Simple Music Player'
        self.__winW = 1300
        self.__winH = 700
        self.__initWindow()
        self.__initUI()
    
    def __initWindow(self):
        self.title(self.__winTitle)
        self.geometry(f'{self.__winW}x{self.__winH}')
        self.resizable(0, 0)

    def __initUI(self):
        self.slider = ttk.Scale(self, length=100).pack()
        

Mainwindow().mainloop()