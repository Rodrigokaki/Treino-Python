from tkinter import *
from tkinter import ttk

def main():
    for i in input_usuario.get():
        if i == '0' or i == '1':
            sucesso = 1
            continue
        else:
            resposta.set('Digite apenas numeros binarios!')
            break
    casa, numero = 1, 0
    for i in input_usuario.get()[::-1]:
        if i == '1':
            for n in range(casa):
                numero += 1
                casa += 1
        elif i == '0':
            for n in range(casa):
             casa += 1
    if sucesso == 1:
        resposta.set(numero)    
        
root = Tk()
root.title('Conversor binario')
ttk.Label(root, text= 'Digite um numero binario:').grid(column=0, row=0)
ttk.Label(root, text= 'Numero decimal:').grid(column=0, row=1)

input_usuario = StringVar()
ttk.Entry(root, textvariable= input_usuario).grid(column=1, row=0)

ttk.Button(root, text='Enter', command=main).grid(column=2, row=0)

resposta = StringVar()
ttk.Label(root, textvariable= resposta).grid(column=1, row=1, sticky='w')

root.mainloop()