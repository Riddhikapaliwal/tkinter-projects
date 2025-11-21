#celcius to farenheit converter
from tkinter import *

root=Tk()
root.title("celcius to farenheit")

def calculate(*args):
    value=float(celcius.get())
    farenheit.set(round(value*(9/5) + 32,2))

mainframe=Frame(root,bg="darkblue")
mainframe.grid(row=0,column=0,sticky=(N,W,E,S),padx=10,pady=10)

celcius=StringVar()
farenheit=StringVar()

entry=Entry(mainframe,textvariable=celcius,font=("Helvetica",12,"bold"))
entry.grid(column=2,row=1,sticky=E,padx=5,pady=5)
label1=Label(mainframe,text="celcius",bg="darkblue",fg="white",font=("Helvetica", 12, "bold")).grid(column=3,row=1,sticky=W,padx=5,pady=5)

label2=Label(mainframe,text="is",fg="white",bg="darkblue",font=("Helvetica", 12, "bold")).grid(column=2,row=2,sticky=(N,W,E,S),padx=5)

label3=Label(mainframe,text="farenheit",bg="darkblue",fg="white",font=("Helvetica",12,"bold")).grid(column=3,row=3,sticky=W,padx=5,pady=5)
label4=Label(mainframe,textvariable=farenheit,font=("Helvetica",12,"bold")).grid(column=2, row=3,sticky=E,padx=5,pady=5)

button=Button(mainframe,text="calculate",command=calculate,bg="green",font=("Helvetica", 12, "bold"),fg="white")
button.grid(column=3,row=4, sticky=(N,S,E,W),padx=10,pady=10)

entry.focus()
root.bind("<Return>",calculate)

root.rowconfigure(0, weight=1)
root.columnconfigure(0,weight=1)

root.mainloop()