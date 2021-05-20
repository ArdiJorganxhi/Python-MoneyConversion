from tkinter import *


dritare = Tk()
dritare.title('Projekti')
dritare.geometry('300x300')

lbl = Label(dritare, text = 'Doviz', font = ('Arial', 20))
lbl.pack()

ent1 = Entry(dritare)
ent1.place(x = 10, y = 55)

var = StringVar()
var.set('Euro')
lista = ['Euro','Dollar','Turkish Lira']

var2 = StringVar()
var2.set('Euro')

option1 = OptionMenu(dritare,var,*lista)
option1.place(x = 90, y = 50)

option2 = OptionMenu(dritare,var2, *lista)
option2.place(x = 160, y = 50)

labelrezultati = Label(dritare, text = '', font = ('Arial', 20) )
labelrezultati.pack(side = LEFT)
def funksioni():
    global var
    global var2
    global labelrezultati
    global ent1

    vlera = int(ent1.get())
    if(var.get() == 'Euro' and var2.get() == 'Euro'):
         labelrezultati.config(text = str(vlera*1) + 'Euro')
    if(var.get() == 'Euro' and var2.get() == 'Dollar'):
         labelrezultati.config(text = str(vlera*1.22)+ 'Dollar')
    if(var.get() == 'Euro' and var2.get() == 'Turkish Lira'):
        labelrezultati.config(text = str(vlera*10.24)+'Turkish Lira')
    if(var.get() == 'Turkish Lira' and var2.get() == 'Euro'):
        labelrezultati.config(text = str(vlera*0.098)+'Euro')
    if(var.get()== 'Dollar' and var2.get() =='Turkish Lira'):
        labelrezultati.config(text = str(vlera*8.38)+'Turkish Lira')
    if(var.get() == 'Turkish Lira' and var2.get() == 'Dollar'):
        labelrezultati.config(text = str(vlera*0.19)+'Dollar')
    if (var.get() == 'Dollar' and var2.get() == 'Dollar'):
            labelrezultati.config(text=str(vlera * 1) + 'Dollar')
    if (var.get() == 'Turkish Lira' and var2.get() == 'Turkish Lira'):
        labelrezultati.config(text=str(vlera * 1) + 'Turkish Lira')
    if (var.get() == 'Dollar' and var2.get() == 'Euro'):
        labelrezultati.config(text=str(vlera * 0.82) + 'Dollar')







button = Button(dritare, text = 'Konverto', command = funksioni)
button.place(x = 200, y = 100)







mainloop()