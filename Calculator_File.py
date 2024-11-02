from tkinter import *

def Button_press(num):
    pass

def Equals():
    pass

def Clear():
    pass

def Delete():
    pass

def PlusOMinus():
    pass

def Percentage():
    pass

#End of Functions


window = Tk()
window.title("Calculator")
window.geometry("400x500")

equation_text=""
equation_label=StringVar()

label=Label(window,textvariable=equation_label , font=('times new roman',20),bg="grey" ,width=24 ,height=2)
label.pack()

frame=Frame(window)
frame.pack()

button_AC=Button(frame,text="AC",font=20,height=4,width=9 ,command=Clear)
button_AC.grid(row=0,column=0)

button_Del=Button(frame,text="Del",font=20,height=4,width=9 ,command=Delete)
button_Del.grid(row=0,column=1)

button_percentage=Button(frame,text="%",font=20,height=4,width=9 ,command=Percentage)
button_percentage.grid(row=0,column=2)

button_division=Button(frame,text="/",font=20,height=4,width=9 ,command=lambda :Button_press("/"))
button_division.grid(row=0,column=3)

button7=Button(frame,text=7,font=20,height=4,width=9,command=lambda :Button_press(7))
button7.grid(row=1,column=0)

button8=Button(frame,text=8,font=20,height=4,width=9,command=lambda :Button_press(8))
button8.grid(row=1,column=1)

button9=Button(frame,text=9,font=20,height=4,width=9,command=lambda :Button_press(9))
button9.grid(row=1,column=2)

button_Mul=Button(frame,text="x",font=20,height=4,width=9,command=lambda :Button_press("*"))
button_Mul.grid(row=1,column=3)

button4=Button(frame,text=4,font=20,height=4,width=9,command=lambda :Button_press(4))
button4.grid(row=2,column=0)

button5=Button(frame,text=5,font=20,height=4,width=9,command=lambda :Button_press(5))
button5.grid(row=2,column=1)

button6=Button(frame,text=6,font=20,height=4,width=9,command=lambda :Button_press(6))
button6.grid(row=2,column=2)

button_sub=Button(frame,text="-",font=20,height=4,width=9,command=lambda :Button_press("-"))
button_sub.grid(row=2,column=3)

button1=Button(frame,text=1,font=20,height=4,width=9,command=lambda :Button_press(1))
button1.grid(row=3,column=0)

button2=Button(frame,text=2,font=20,height=4,width=9,command=lambda :Button_press(2))
button2.grid(row=3,column=1)

button3=Button(frame,text=3,font=20,height=4,width=9,command=lambda :Button_press(3))
button3.grid(row=3,column=2)

button_add=Button(frame,text="+",font=20,height=4,width=9,command=lambda :Button_press("+"))
button_add.grid(row=3,column=3)

button_pom=Button(frame,text="+/-",font=20,height=4,width=9 ,command=PlusOMinus)
button_pom.grid(row=4,column=0)

button0=Button(frame,text=0,font=20,height=4,width=9,command=lambda :Button_press(0))
button0.grid(row=4,column=1)

button_decimal=Button(frame,text=".",font=20,height=4,width=9,command=lambda :Button_press("."))
button_decimal.grid(row=4,column=2)

button_equals=Button(frame,text="=",font=20,height=4,width=9,command=Equals)
button_equals.grid(row=4,column=3)

window.mainloop()