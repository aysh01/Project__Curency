import tkinter as tk
from numerize import *

# Top level window
frame = tk.Tk()
frame.title("Currency Converter")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget


def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    inp1 = inputtxt1.get(1.0, "end-1c")
    inp2 = inputtxt2.get(1.0, "end-1c")

    word = 'dollar' or 'Dollar'
    word1 = 'rupee' or 'rupees' #Case 1

    word12 = 'rupee' or 'rupees'
    word15 = 'dollar' or 'Dollar' #Case 2
    if (word in inp1) and (word1 in inp2):
        num1 = 82  # 1 dollar = `81.71` ~ 82 Rupees.
        ans = int(inp) * int(num1)
        convert = str(ans)
        lbl.config(text="Conversion Rate%"+" from " +inp1+" to "+inp2+": $"+convert)

    elif (word12 in inp1) and (word15 in inp2):
        num12 = 12 #1 rupees = '12' ~ 1dollar
        ans1 = int(inp) * int(num12)
        convert1 = str(ans1)
        lbl.config(text="Conversion Rate%"+" from "+inp1+" to "+inp2+": Rupees "+convert1)


    # TextBox Creation
inputtxt = tk.Text(height=2, width=30)  # Take Value
inputtxt1 = tk.Text(height=2, width=30)  # From Currency
inputtxt2 = tk.Text(height=2, width=30)  # To Currency

inputtxt.pack()
inputtxt1.pack()
inputtxt2.pack()

# Button Creation
printButton = tk.Button(frame, text="Convert", command=printInput)
printButton.pack()
# printButton1.pack()

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
