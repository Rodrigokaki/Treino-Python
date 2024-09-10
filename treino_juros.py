from tkinter import *

def Calcular():
    valor_inicial = variable1.get()
    juros = (variable2.get()*0.01)
    tempo = variable3.get()

    if escolha_juros.get() == 'simples':
        valor_final = valor_inicial + ((valor_inicial*juros)*tempo)
        valor_final = '%.2f'%valor_final
        resultado.set(valor_final)
        label_resultado.update()

    if escolha_juros.get() == 'composto':
        valor_atual = valor_inicial
        for i in range(tempo):
            valor_atual = valor_atual + (valor_atual*juros)
        valor_final = '%.2f'%valor_atual
        resultado.set(valor_final)
        label_resultado.update()



root = Tk()
root.title('Calculador de juros')

Label(root, text='Valor inicial: ',anchor=E).grid(column=0,row=0,pady=(5,10))
Label(root, text='Juros por mes(%): ', anchor=E).grid(column=0,row=1,pady=(10,10),padx=(5,0))
Label(root, text='Meses: ', anchor=E).grid(column=0,row=2,pady=(10,10))
Label(root, text='Valor final: ', anchor=E).grid(column=0,row=4,pady=(10,10))

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
Entry(root, width=30,textvariable=variable1).grid(columnspan=2,column=1,row=0)
Entry(root, width=30,textvariable=variable2).grid(columnspan=2,column=1,row=1)
Entry(root, width=30,textvariable=variable3).grid(columnspan=2,column=1,row=2)

escolha_juros = StringVar()
Radiobutton(root,text= 'Juros simples', variable= escolha_juros, value= 'simples').grid(column=1,row=3)
Radiobutton(root,text= 'Juros composto', variable= escolha_juros, value= 'composto').grid(column=2,row=3)
escolha_juros.set('simples')

resultado = IntVar()
label_resultado = Label(root,textvariable=resultado,anchor=W)
label_resultado.grid(columnspan=2,column=1,row=4)

Button(root,text='Enviar',command=Calcular).grid(column=3,row=4,padx=(0,10))

root.mainloop()