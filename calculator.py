from tkinter import *

root=Tk()
root.title("Calculator")

entry=Entry(root, font=("Arial",20,"bold"), width=20, borderwidth=5 ,bg="lightblue")
entry.grid(row=0,column=0,padx=5, pady=5,columnspan=4)
entry.focus()

def click(value):
    entry.insert(END, value)

def evaluate(*args):
    result=eval(entry.get())
    entry.delete(0,END)
    entry.insert(0, result)

def clear():
  entry.delete(0,END)


button=[1,2,3,"/",4,5,6,"*",7,8,9,"-",0,".","=","+"]
row=1
col=0

for text in button:
    if text=="=":
        btn=Button(root,font=("Arial",18,"bold"),command=evaluate,text=text,width=5,height=2,fg="blue")

    else:
        btn=Button(root, font=("Arial",18,"bold"),text=text, command=lambda t=text: click(t),width=5,height=2,fg="blue")

    btn.grid(row=row,column=col,padx=2,pady=2)
    col=col+1
    if col==4:
        col=0
        row=row+1

btn1=Button(root,text="clear",font=("Arial",18,"bold"),command=clear,borderwidth=2,width=5,height=2,fg="blue")
btn1.grid(row=row,column=0,padx=2,pady=2)
root.bind("<Return>",evaluate)
root.mainloop()
