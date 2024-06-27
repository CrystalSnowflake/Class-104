from tkinter import * 
from tkinter import font 
#create root window 
root = Tk() 
#get all the supported font families 
list_fonts = list(font.families()) 

for i in range(len(list_fonts)):
    print(list_fonts[i])