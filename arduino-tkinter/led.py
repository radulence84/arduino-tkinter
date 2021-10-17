import serial

import tkinter as tk 
from tkinter import *

commPort = '/dev/ttyUSB0'
ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)

def turnOnLED():
    ser.write(b'0')

def turnOffLED(): 
    ser.write(b'1')
    
def turnOnLED1():
    ser.write(b'2')

def turnOffLED1(): 
    ser.write(b'3')

# creating tkinter window 
root = Tk() 
root.title('Blink GUI')

btn_On1= tk.Button(root, text="Ukljuci LED", command=turnOnLED)
btn_On1.grid(row=0, column=0)

btn_Off1 = tk.Button(root, text="Iskljuci LED", command=turnOffLED)
btn_Off1.grid(row=0, column=1)

btn_On2= tk.Button(root, text="Ukljuci LED1", command=turnOnLED1)
btn_On2.grid(row=1, column=0)

btn_Off2 = tk.Button(root, text="Iskljuci LED1", command=turnOffLED1)
btn_Off2.grid(row=1, column=1)

root.geometry("350x350")
root.mainloop()
