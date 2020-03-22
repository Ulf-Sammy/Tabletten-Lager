
import datetime
import sys
from tkinter import *
from classFenster import MyApp

def main():
    x = True
    root = Tk()

    while  x:
        App = MyApp()
        root.mainloop()
        x = App.Ende
        
if __name__ == '__main__':
    main()