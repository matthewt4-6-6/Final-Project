import tkinter as tk 
from tkinter import  *
from tkinter import ttk


curX = 0
curY = 0


window = tk.Tk()
window.title("tk")
window.geometry("700x900")
   
attempts = 6
wordguess = 5






def updateBox(keyVal):
    print(f'they clicked on {keyVal}')
    # update the nextbox with the keyVal
    # increment the nextbox
    print(f'writing to box {curX} {curY}')
    #increase curY to be the next value but if it's too big reset it to 0 and increase curX

def clickedQ(e):
    print(e)
    print('they clicked Q')
    updateBox('q')
    label["text"] = "Q"
    
def clickedW(e):
    print(e)
    print('they clicked W')
    updateBox('w')
    label["text"] = "W"


def clickedE(e):
    print(e)
    print('they clicked E')
    updateBox('e')
    label["text"] = "E"

def clickedR(e):
    print(e)
    print('they clicked R')
    updateBox('r')
    label["text"] = "R"

def clickedT(e):
    print(e)
    print('they clicked T')
    updateBox('t')
    label["text"] = "T"

def clickedY(e):
    print(e)
    print('they clicked Y')
    updateBox('y')
    label["text"] = "Y"

def clickedU(e):
    print(e)
    print('they clicked U')
    updateBox('u')
    label["text"] = "U"

def clickedI(e):
    print(e)
    print('they clicked I')
    updateBox('i')
    label["text"] = "I"

def clickedO(e):
    print(e)
    print('they clicked O')
    updateBox('o')
    label["text"] = "O"

def clickedP(e):
    print(e)
    print('they clicked P')
    updateBox('p')
    label["text"] = "P"

def clickedA(e):
    print(e)
    print('they clicked A')
    updateBox('a')
    label["text"] = "A"

def clickedS(e):
    print(e)
    print('they clicked S')
    updateBox('s')
    label["text"] = "S"

def clickedD(e):
    print(e)
    print('they clicked D')
    updateBox('d')
    label["text"] = "D"

def clickedF(e):
    print(e)
    print('they clicked F')
    updateBox('f')
    label["text"] = "F"
    
def clickedG(e):
    print(e)
    print('they clicked G')
    updateBox('g')
    label["text"] = "G"
    
def clickedH(e):
    print(e)
    print('they clicked H')
    updateBox('h')
    label["text"] = "H"
    
def clickedJ(e):
    print(e)
    print('they clicked J')
    updateBox('j')
    label["text"] = "J"
    
def clickedK(e):
    print(e)
    print('they clicked K')
    updateBox('k')
    label["text"] = "K"
    
def clickedL(e):
    print(e)
    print('they clicked L')
    updateBox('l')
    label["text"] = "L"
    
def clickedZ(e):
    print(e)
    print('they clicked Z')
    updateBox('z')
    label["text"] = "Z"
    
def clickedX(e):
    print(e)
    print('they clicked X')
    updateBox('x')
    label["text"] = "X"
    
def clickedC(e):
    print(e)
    print('they clicked C')
    updateBox('c')
    label["text"] = "C"
    
def clickedV(e):
    print(e)
    print('they clicked V')
    updateBox('y')
    label["text"] = "V"
    
def clickedB(e):
    print(e)
    print('they clicked B')
    updateBox('b')
    label["text"] = "B"
    
def clickedN(e):
    print(e)
    print('they clicked N')
    updateBox('n')
    label["text"] = "N"
    
def clickedM(e):
    print(e)
    print('they clicked M')
    updateBox('m')
    label["text"] = "M"
    
def clickedENTER(e):
    print(e)
    print('they clicked ENTER')
    label["text"] = "q"
    

def clickedDELETE(e):
    print(e)
    print('they clicked DELETE')
    label["text"] = ""
    
##keyboard text

q = tk.Button(window, text = "Q", font = 10, borderwidth = 5, background = "gray")
w = tk.Button(window, text = "W", font = 10, borderwidth = 5, background = "gray")
e = tk.Button(window, text = "E", font = 10, borderwidth = 5, background = "gray")
r = tk.Button(window, text = "R", font = 10, borderwidth = 5, background = "gray")
t = tk.Button(window, text = "T", font = 10, borderwidth = 5, background = "gray")
y = tk.Button(window, text = "Y", font = 10, borderwidth = 5, background = "gray")
u = tk.Button(window, text = "U", font = 10, borderwidth = 5, background = "gray")
i = tk.Button(window, text = "I", font = 10, borderwidth = 5, background = "gray")
o = tk.Button(window, text = "O", font = 10, borderwidth = 5, background = "gray")
p = tk.Button(window, text = "P", font = 10, borderwidth = 5, background = "gray")
a = tk.Button(window, text = "A", font = 10, borderwidth = 5, background = "gray")
s = tk.Button(window, text = "S", font = 10, borderwidth = 5, background = "gray")
d = tk.Button(window, text = "D", font = 10, borderwidth = 5, background = "gray")
f = tk.Button(window, text = "F", font = 10, borderwidth = 5, background = "gray")
g = tk.Button(window, text = "G", font = 10, borderwidth = 5, background = "gray")
h = tk.Button(window, text = "H", font = 10, borderwidth = 5, background = "gray")
j = tk.Button(window, text = "J", font = 10, borderwidth = 5, background = "gray")
k = tk.Button(window, text = "K", font = 10, borderwidth = 5, background = "gray")
l = tk.Button(window, text = "L", font = 10, borderwidth = 5, background = "gray")
enter = tk.Button(window, text = "ENTER", font = 10, borderwidth = 5, background = "gray")
z = tk.Button(window, text = "Z", font = 10, borderwidth = 5, background = "gray")
x = tk.Button(window, text = "X", font = 10, borderwidth = 5, background = "gray")
c = tk.Button(window, text = "C", font = 10, borderwidth = 5, background = "gray")
v = tk.Button(window, text = "V", font = 10, borderwidth = 5, background = "gray")
b = tk.Button(window, text = "B", font = 10, borderwidth = 5, background = "gray")
n = tk.Button(window, text = "N", font = 10, borderwidth = 5, background = "gray")
m = tk.Button(window, text = "M", font = 10, borderwidth = 5, background = "gray")
delete = tk.Button(window, text = "DELETE", font = 10, borderwidth = 5, background = "gray")

q.bind("<Button>",clickedQ)
w.bind("<Button>",clickedW)
e.bind("<Button>",clickedE)
r.bind("<Button>",clickedR)
t.bind("<Button>",clickedT)
y.bind("<Button>",clickedY)
u.bind("<Button>",clickedU)
i.bind("<Button>",clickedI)
o.bind("<Button>",clickedO)
p.bind("<Button>",clickedP)
a.bind("<Button>",clickedA)
s.bind("<Button>",clickedS)
d.bind("<Button>",clickedD)
f.bind("<Button>",clickedF)
g.bind("<Button>",clickedG)
h.bind("<Button>",clickedH)
j.bind("<Button>",clickedJ)
k.bind("<Button>",clickedK)
l.bind("<Button>",clickedL)
z.bind("<Button>",clickedZ)
x.bind("<Button>",clickedX)
c.bind("<Button>",clickedC)
v.bind("<Button>",clickedV)
b.bind("<Button>",clickedB)
n.bind("<Button>",clickedN)
m.bind("<Button>",clickedM)
enter.bind("<Button>",clickedENTER)
delete.bind("<Button>",clickedDELETE)

row = []
for ii in range(6):
    row.append([])
    for iii in range(5):
        row[ii].append([])


        


print(row)
#row1ofboxes
row[0][0]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[0][1]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[0][2]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[0][3]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[0][4]= label = tk.Label(window,borderwidth = 25, background = "gray",)

#row2ofboxes
row[1][0]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[1][1]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[1][2]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[1][3]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[1][4]= label = tk.Label(window,borderwidth = 25, background = "gray",)


#row3ofboxes
row[2][0]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[2][1]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[2][2]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[2][3]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[2][4]= label = tk.Label(window,borderwidth = 25, background = "gray",)


#row4ofboxes
row[3][0]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[3][1]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[3][2]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[3][3]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[3][4]= label = tk.Label(window,borderwidth = 25, background = "gray",)


#row5ofboxes
row[4][0]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[4][1]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[4][2]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[4][3]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[4][4]= label = tk.Label(window,borderwidth = 25, background = "gray",)


#row6ofboxes
row[5][0]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[5][1]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[5][2]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[5][3]= label = tk.Label(window,borderwidth = 25, background = "gray",)
row[5][4]= label = tk.Label(window,borderwidth = 25, background = "gray",)


for a1 in range(0,5):
    for b1 in range(0,6):
        row[b1][a1].place(x = 165 + 80*a1, y = 150 + 70*b1, width=60, height = 60)


##keyboard arrangement
q.place(x = 100, y = 600, width=40)
w.place(x = 150, y = 600, width=40)
e.place(x = 200, y = 600, width=40)
r.place(x = 250, y = 600, width=40)
t.place(x = 300, y = 600, width=40)
y.place(x = 350, y = 600, width=40)
u.place(x = 400, y = 600, width=40)
i.place(x = 450, y = 600, width=40)
o.place(x = 500, y = 600, width=40)
p.place(x = 550, y = 600, width=40)
a.place(x = 125, y = 650, width=40)
s.place(x = 175, y = 650, width=40)
d.place(x = 225, y = 650, width=40)
f.place(x = 275, y = 650, width=40)
g.place(x = 325, y = 650, width=40)
h.place(x = 375, y = 650, width=40)
j.place(x = 425, y = 650, width=40)
k.place(x = 475, y = 650, width=40)
l.place(x = 525, y = 650, width=40)
enter.place(x=100,y=700,width= 60)
delete.place(x = 530, y = 700, width=60)
z.place(x = 175, y = 700, width=40)
x.place(x = 225, y = 700, width=40)
c.place(x = 275, y = 700, width=40)
v.place(x = 325, y = 700, width=40)
b.place(x = 375, y = 700, width=40)
n.place(x = 425, y = 700, width=40)
m.place(x = 475, y = 700, width=40)

##first row
 

main = PhotoImage(file="wordlelogo1.png")
photo = tk.Label(window, image=main)

photo.place(x=0, y = 10)

window.mainloop()