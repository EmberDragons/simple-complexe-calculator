# Créé par isbillard, le 11/10/2024 en Python 3.7
import tkinter as tk
class Complex:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def z_barre(self):
        z = Complex(self.a, -self.b)
        return z

    def addition(self, z2):
        z = Complex(self.a+z2.a, self.b+z2.b)
        return z
    def substraction(self, z2):
        z = Complex(self.a-z2.a, self.b-z2.b)
        return z
    def multiplication(self, z2):
        z = Complex(self.a*z2.a-self.b*z2.b, self.a*z2.b+self.b*z2.a)
        return z
    def division(self, z2):
        """z1/z2 = a1 + i * b1 / a2 + i * b2 = a1*(a2+i*-b2) / (a2+i*b2)*(a2+i*-b2)  +  i * b2*(a2+i*-b2)/ (a2+i*b2)*(a2+i*-b2)"""
        #premiere partie (en haut)
        a1 = self.multiplication(z2.z_barre()).a
        b1 = self.multiplication(z2.z_barre()).b

        #deuxieme partie (en bas)
        a2 = z2.multiplication(z2.z_barre()).a
        #to not divide by 0
        reel = 0
        imaginary = 0
        if a2!=0:
            reel = a1/a2
            imaginary = b1/a2

        z = Complex(round(reel, 2), round(imaginary, 2))
        return z

    def __str__(self):
        if self.b>0:
            return str(f"{self.a} + {self.b}i")
        else: #negative
            return str(f"{self.a} - {-self.b}i")


def return_complex(l1):
    signs1=[1,1]
    if "-" in l1:
        if l1[0] == '-':
            signs1[0] = -1
            l1=l1[1:] #we skip the first sign
        if "-" in l1: #second - sign
            signs1[1] = -1
    l1=l1.replace('-', '+').split('+')

    cplx1 = e1.get()
    if l1[0] == '':
        cplx1 = Complex(0, 0)
    elif len(l1) == 1:
        if 'i' not in l1[0]:
            cplx1 = Complex(signs1[0]*float(l1[0]), 0)
        else:
            l1[0]=l1[0][:-1]
            cplx1 = Complex(0,signs1[0]*float(l1[0]))
    else:
        if 'i' in l1[1]:
            l1[1]=l1[1][:-1]
        cplx1 = Complex(signs1[0]*float(l1[0]), signs1[1]*float(l1[1]))
    return cplx1


def show_result():
    #numbers 1 and 2 treatment
    l1=e1.get()
    cplx1 = return_complex(l1)

    l2=e2.get()
    cplx2 = return_complex(l2)

    #the actual operation
    operation_s = v.get()
    ans="nothin' yet"
    if operation_s == op[0][1]:
        ans = str(cplx1.addition(cplx2))
    if operation_s == op[1][1]:
        ans = str(cplx1.substraction(cplx2))
    if operation_s == op[2][1]:
        ans = str(cplx1.multiplication(cplx2))
    if operation_s == op[3][1]:
        if cplx2.a != 0 or cplx2.b!=0:
            ans = str(cplx1.division(cplx2))
        else:
            ans="division by 0 not allowed!"
    #avoid problems
    filler = (100-len(ans))*' '
    tk.Label(master, text=(filler[:len(filler)//2]+ans+filler[len(filler)//2:])).grid(row=8, column=1)

"""window's set up"""
master = tk.Tk()
master.config(cursor="circle")

#ex
tk.Label(master, text="ex. notation: 1+5i or 5-9i or 5 or 10i").grid(row=0)

#the 2 complexe
tk.Label(master, 
         text="First Complex").grid(row=1)
tk.Label(master, 
         text="Second Complex").grid(row=2)

#operation choice
v = tk.IntVar()
v.set(1)  # initializing the choice

op = [("addition", 101), ("substraction", 102), ("multiplication", 103), ("division", 104)]
row=3
for operation in op:
    tk.Radiobutton(master, 
                   text=operation[0],
                   padx = 20, 
                   variable=v, 
                   value=operation[1],
                   command=show_result).grid(row=row)
    row+=1

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

master.mainloop()