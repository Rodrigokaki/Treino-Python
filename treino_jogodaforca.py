from tkinter import *
import random

PATH = ""

def start_game():
    pegar_palavra_aleatoria()
    global palavra_oculta
    coluna = 0
    for traco in palavra_aleatoria:
        palavra_oculta = Label(root,text="_",font=25)
        palavra_oculta.grid(row=0, column=coluna,pady=(30,30))
        coluna += 1
    global acertos_total
    acertos_total = 0


def pegar_palavra_aleatoria():
    palavras = []
    path = open(PATH,'r')
    for linha in path:
        linha = linha.strip()
        linha = linha.lower()
        palavras.append(linha)
    global palavra_aleatoria
    palavra_aleatoria = random.choice(palavras)
    path.close

def Enviar():
    chute = usuario_chute.get()
    entrada.delete(0,'end')
    acerto = 0
    casa = 0
    global acertos_total
    for i in palavra_aleatoria:
        if i == chute:
            Label(root, text=i,font=25).grid(row=0,column=casa,pady=(24,30))
            acerto = 1
            acertos_total +=1
            casa += 1
        else:
            casa += 1
    if acerto == 0:
        global erros
        erros += 1
        Label(root, text='Erros: '+str(erros)).grid(row=0,column=10,columnspan=3,pady=(60,0))
        global chutes_display
        chutes_display += chute+', '
        Label(root, text = chutes_display).grid(row=0,column=0,sticky='n',columnspan=15)
    if acertos_total == len(palavra_aleatoria):
        ganhou()
    if erros > 6:
        perdeu()


def ganhou():
    Frame(root,bg='black',width=200,height=120).grid(column=0,row=0,columnspan=15,rowspan=2)
    Label(root,bg='black',fg='white',font=40,text='Voce ganhou!').grid(column=0,row=0,columnspan=15,rowspan=2,pady=(20,40))

def perdeu():
    Frame(root,bg='black',width=200,height=120).grid(column=0,row=0,columnspan=15,rowspan=2)
    Label(root,bg='black',fg='white',font=40,text='Voce perdeu =(').grid(column=0,row=0,columnspan=15,rowspan=2,pady=(20,40))
    Label(root,bg='black',fg='white',font=40,text='Era: '+palavra_aleatoria).grid(column=0,row=0,columnspan=15,rowspan=2,pady=(50,10))

    

        


erros = 0
chutes_display = ""    
root = Tk()
root.title('Jogo da forca')
start_game()

Label(root, text= 'Chute uma letra:').grid(column=1,row=1,columnspan=6)
Label(root, text='Erros: '+str(erros)).grid(row=0,column=10,columnspan=3,pady=(60,0))

usuario_chute = StringVar()
entrada = Entry(root, borderwidth= 2, width=5,textvariable=usuario_chute)
entrada.grid(column=7,row=1,columnspan=2)

Botao = Button(root, command=Enviar, text='Enviar')
Botao.grid(column=11,row=1,columnspan=3)


root.mainloop()

