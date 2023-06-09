from tkinter import *
import random
import string
import pyperclip

#creamos la ventana
root = Tk()
root.title("Generador de contraseñas")
root.geometry("400x400")
root.resizable(0,0)
root.config(bg="black")

def generar():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    longitud = 16
    password = "".join(random.choice(caracteres) for i in range(longitud))
    contraseña.set(password)

def copiar():
    pyperclip.copy(contraseña.get())

def salir():
    root.destroy()

contraseña = StringVar()
boton_generar = Button(root, text="Generar", command=generar, bg="white", fg="black", font=("Arial", 15)).place(x=150, y=50)
boton_copiar = Button(root, text="Copiar", command=copiar, bg="white", fg="black", font=("Arial", 15)).place(x=150, y=100)
etiqueta = Entry(root, textvariable=contraseña, bg="white", fg="black", font=("Arial", 15)).place(x=50, y=200)
boton_salir = Button(root, text="Salir", command=salir, bg="red", fg="white", font=("Arial", 15)).place(x=150, y=150)
boton_limpiar = Button(root, text="Limpiar", command=lambda: contraseña.set(""), bg="white", fg="black", font=("Arial", 15)).place(x=250, y=150)
root.mainloop()