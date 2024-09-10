from tkinter import *

root = Tk()
root.title('Calculadora')

entry = Entry(root,width=50,bg="white")
entry.grid(column=0,row=0,columnspan=5,rowspan=2, padx=8, pady=8)


def botao_click(numero):
    numero_atual = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, numero_atual+numero)
    
def funcao(a):
    global number_stored
    number_stored = entry.get()
    entry.delete(0,'end')
    global selection
    selection = a

def igual():
        global result
        global selection
        if selection == 'soma':
            result = int(number_stored) + int(entry.get())
            entry.delete(0,'end')
            entry.insert(0, result)
            selection = None
        elif selection == 'multiplicacao':
            result = int(number_stored) * int(entry.get())
            entry.delete(0,'end')
            entry.insert(0, result)
            selection = None
        elif selection == 'menos':
            result = int(number_stored) - int(entry.get())
            entry.delete(0,'end')
            entry.insert(0, result)
            selection = None
        elif selection == 'divisao':
            result = int(number_stored) / int(entry.get())
            result = round(result)
            entry.delete(0,'end')
            entry.insert(0, result)
            selection = None
        
def apagar():
    quantos = 0
    for i in entry.get():
        quantos += 1
    entry.delete(quantos-1)

def ac():
    entry.delete(0,'end')
    global number_stored
    number_stored = 0


botao1 = Button(root, text="1", command=lambda: botao_click('1'),padx=30, pady=10).grid(column=0,row=4)
botao2 = Button(root, text="2", command=lambda: botao_click('2'),padx=30, pady=10).grid(column=1,row=4)
botao3 = Button(root, text="3", command=lambda: botao_click('3'),padx=30, pady=10).grid(column=2,row=4)
botao4 = Button(root, text="4", command=lambda: botao_click('4'),padx=30, pady=10).grid(column=0,row=3)
botao5 = Button(root, text="5", command=lambda: botao_click('5'),padx=30, pady=10).grid(column=1,row=3)
botao6 = Button(root, text="6", command=lambda: botao_click('6'),padx=30, pady=10).grid(column=2,row=3)
botao7 = Button(root, text="7", command=lambda: botao_click('7'),padx=30, pady=10).grid(column=0,row=2)
botao8 = Button(root, text="8", command=lambda: botao_click('8'),padx=30, pady=10).grid(column=1,row=2)
botao9 = Button(root, text="9", command=lambda: botao_click('9'),padx=30, pady=10).grid(column=2,row=2)
botao0 = Button(root, text="0", command=lambda: botao_click('0'),padx=30, pady=10).grid(column=1,row=5)
botaomais = Button(root, text="+", command=lambda: funcao('soma'),padx= 30, pady= 10).grid(column=3, row=3)
botaoigual = Button(root, text='=', command=igual,padx=30, pady=10).grid(column=4, row=5)
botaoback = Button(root, text='🠔', command=apagar, padx=30, pady=10).grid(column=3, row=2)
botaomultiplicacao = Button(root, text='x', command=lambda: funcao('multiplicacao'), padx=30, pady=10).grid(column=3,row=4)
botaomenos = Button(root, text="-", command=lambda: funcao('menos'),padx= 30, pady= 10).grid(column=4, row=3)
botaodivisao = Button(root, text="/", command=lambda: funcao('divisao'),padx= 30, pady= 10).grid(column=4, row=4)
botaoac = Button(root, text="AC", command= ac,padx= 30, pady= 10).grid(column=4, row=2)


root.mainloop()