from tkinter import *

lista = {'aatrox':'Dados do Aatrox: \nTelefone: 45675435 \nRota: Top',
'ahri': 'Dados da Ahri: \nTelefone: 97864335 \nRota: Mid',
'akali':'Dados da Akali: \nTelefone: 1223156 \nRota: Mid,Top',
'akshan':'Dados do Akshan: \nTelefone: 465443897 \nRota: Mid',
'alistar':'Dados do Alistar: \nTelefone: 7982134 \nRota: Sup'}


def info(nome):
    Label(root, text= lista[nome]).grid(column=1, row=0, rowspan=50, padx=(100,0), pady=(0,240))

root = Tk()
root.title('Lista de nomes')
frame = Frame(root, borderwidth=2, height=300, width=200,relief='sunken')
frame.grid(column=1, row=0, rowspan=50,padx=(100,0))


linha = 0
for i in lista:
    Button(root, text= i, command=lambda x=i: info(x)).grid(column=0, row=linha)
    linha += 1


root.mainloop()