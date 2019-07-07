from tkinter import *
top = Tk()
top.title("calculator")
top.minsize(300,200)
first_number = Label(text ="number")
first_number.pack()
first_numberbox = Entry()
first_numberbox.pack()


second_number = Label(text="number")
second_number.pack()
second_numberbox = Entry()
second_numberbox.pack()
def addnumbers():
    number1 = float(first_numberbox.get())
    number2 = float(second_numberbox.get())
    result = number1 + number2
    resultlabel = Label(text= "The result is :\n"+str(result))
    resultlabel.pack()


button = Button(text ="add",command= addnumbers)
button.pack()



top.mainloop()
