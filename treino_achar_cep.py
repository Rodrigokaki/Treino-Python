from tkinter import *
import requests


def buscar():
    usuario = cep_usuario.get()
    url = requests.get('https://viacep.com.br/ws/{cep}/json/'.format(cep=usuario))
    if url.status_code == 200:
        print('Sucesso')
    elif url.status_code == 400:
        print('Erro 400')

    endereco = url.json()
    endereco = dict(endereco)
    display = ''
    texto.delete(1.0, END)
    for key,value in endereco.items():
        texto.insert(END, key+' : '+ value+'\n')


    # texto.insert(END, endereco)

root = Tk()
root.configure(bg='#06496A')
root.geometry('350x300')
root.title('CEP Finder minimalista')

Label(root, text='CEP:').grid(column=0,row=0,sticky='W',pady=(0,2),padx=(5))

cep_usuario = StringVar()
cep_input = Entry(root, width= 40, textvariable=cep_usuario)
cep_input.grid(column=0, row=0, padx=(0,10))

Button(root, text='Buscar',command=buscar).grid(column=0,row=0,pady=(0,2),padx=(300,0))

texto = Text(root, height=15, width=35)
texto.grid(column=0,row=1,pady=(20))

root.mainloop()
