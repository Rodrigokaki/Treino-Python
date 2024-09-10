from doctest import testfile
from tkinter import *
import random

def novo_jogo():
    jogo = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

    add2(jogo)

    return jogo


    
    
    


def add2(jogo):

    linha = random.randint(0,3)
    coluna = random.randint(0,3)

    while jogo[linha][coluna] != 0:
        linha = random.randint(0,3)
        coluna = random.randint(0,3)
    
    jogo[linha][coluna] = 2




def mover(jogo):
    movido = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

    for linha in range(4):
        casa = 0
        for coluna in range(4):
            if jogo[linha][coluna] != 0:
                movido[linha][casa] = jogo[linha][coluna]
                casa += 1
    
    for linha in range(4):
        for coluna in range(3):
            if movido[linha][coluna] != 0 and movido[linha][coluna] == movido[linha][coluna+1]:
                movido[linha][coluna] = movido[linha][coluna]*2
                movido[linha][coluna+1] = 0
    movido2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for linha in range(4):
        casa = 0
        for coluna in range(4):
            if movido[linha][coluna] != 0:
                movido2[linha][casa] = movido[linha][coluna]
                casa += 1
    movido = movido2


    return movido



def tecla_mover(tecla,jogo):
    global jogo_atual
    molde = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

    if tecla == 'w' and w_disponivel == 1:
        print('w')
        for i in range(4):
            for j in range(4):
                molde[j][i] = jogo[i][j]
        molde = mover(molde)
        for i in range(4):
            for j in range(4):
                jogo_atual[j][i] = molde[i][j]
        add2(jogo_atual)
        jogo_estado(jogo_atual)
        display(jogo_atual)

    if tecla == 'a' and a_disponivel == 1:
        print('a')
        jogo_atual = mover(jogo)
        add2(jogo_atual)
        jogo_estado(jogo_atual)
        display(jogo_atual)

    if tecla == 's' and s_disponivel == 1:
        print('s')
        l = -1
        for i in range(3,-1,-1):
            k = 0
            l += 1
            for j in range(3,-1,-1):
                molde[k][l] = jogo[i][j]
                k += 1
        molde = mover(molde)
        l = -1
        for i in range(3,-1,-1):
            k = 0
            l += 1
            for j in range(3,-1,-1):
                jogo_atual[k][l] = molde[i][j]
                k += 1
        add2(jogo_atual)
        jogo_estado(jogo_atual)
        display(jogo_atual)

    if tecla == 'd' and d_disponivel == 1:
        print('d')
        for i in range(4):
            k = 0
            for j in range(3,-1,-1):
                molde[i][k] = jogo[i][j]
                k += 1
        molde = mover(molde)
        for i in range(4):
            k = 0
            for j in range(3,-1,-1):
                jogo_atual[i][k] = molde[i][j]
                k += 1
        add2(jogo_atual)
        jogo_estado(jogo_atual)
        display(jogo_atual)




def display(jogo):
    for i in range(4):
        for j in range(4):
            display = jogo[i][j]
            if display == 0:
                display = ''
                cor_display = '#938780'
            if display == 2:
                cor_display = '#EABCB1'
            if display == 4:
                cor_display = '#EAA18F'
            if display == 8:
                cor_display = '#EE8368'
            if display == 16:
                cor_display = '#EA5A36'
            if display == 32:
                cor_display = '#DB380F'
            if display == 64:
                cor_display = '#751801'
            if display == 128:
                cor_display = '#D3DD5A'
            if display == 256:
                cor_display = '#C6D41F'
            if display == 512:
                cor_display = '#899402'
            if display == 1024:
                cor_display = '#464B09'
            if display == 2048:
                cor_display = '#000000'

            Label(root, text=display,fg='white',bg=(cor_display),font=25,height=5,width=10).grid(column=j,row=i)




def jogo_estado(jogo):
    molde = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    quantidade_0 = 0
    global w_disponivel
    w_disponivel = 1
    global a_disponivel
    a_disponivel = 1
    global s_disponivel
    s_disponivel = 1
    global d_disponivel
    d_disponivel = 1
    bloquear_tecla = True
    ganhou = False
    ainda_da = False
    for i in range(4):
        for j in range(4):
            if jogo[i][j] == 2048:
                ganhou = True
            elif jogo[i][j] == 0:
                quantidade_0 += 1

    if quantidade_0 > 0:
        ainda_da = True
    
    #a
    for i in range(4):
        for j in range(4):
            if jogo[i][j] != 0 and jogo[i][j] == jogo[i][j-1] and j >=1:
                ainda_da = True
                bloquear_tecla = False
    if quantidade_0 == 0 and bloquear_tecla == True:
        a_disponivel = 0
        print('Cancelando a tecla a')
    bloquear_tecla = True

    

    #w
    for i in range(4):
        for j in range(4):
            molde[j][i] = jogo[i][j]
    for i in range(4):
        for j in range(4):
            if molde[i][j] != 0 and molde[i][j] == molde[i][j-1] and j >=1:
                ainda_da = True
                bloquear_tecla = False
    if quantidade_0 == 0 and bloquear_tecla == True:
        w_disponivel = 0
        print('Cancelando a tecla w')
    bloquear_tecla = True

    molde = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    
    #s
    l = -1
    for i in range(3,-1,-1):
        k = 0
        l += 1
        for j in range(3,-1,-1):
            molde[k][l] = jogo[i][j]
            k += 1
    for i in range(4):
        for j in range(4):
            if molde[i][j] != 0 and molde[i][j] == molde[i][j-1] and j >=1:
                ainda_da = True
                bloquear_tecla = False
    if quantidade_0 == 0 and bloquear_tecla == True:
        s_disponivel = 0
        print('Cancelando a tecla s')
    bloquear_tecla = True

            
    molde = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

    #d
    for i in range(4):
            k = 0
            for j in range(3,-1,-1):
                molde[i][k] = jogo[i][j]
                k += 1
    for i in range(4):
        for j in range(4):
            if molde[i][j] != 0 and molde[i][j] == molde[i][j-1] and j >=1:
                ainda_da = True
                bloquear_tecla = False
    if quantidade_0 == 0 and bloquear_tecla == True:
        d_disponivel = 0
        print('Cancelando a tecla d')
    bloquear_tecla = True

    
    if ganhou == True:
        while True:
            Label(root,text='Voce Ganhou =)',bg='black',fg='white',font=40,height=25,width=50).grid(columnspan=4,rowspan=4,column=0,row=0)
    elif ainda_da == True:
        print('Ainda da')
    else:
        Label(root,text='Voce perdeu =(',bg='black',fg='white',font=40,height=25,width=50).grid(columnspan=4,rowspan=4,column=0,row=0)
        print('Perdeu')

    
w_disponivel = 1
a_disponivel = 1
s_disponivel = 1
d_disponivel = 1

jogo_atual = novo_jogo()

root = Tk()
root.title('2048')
root.configure(bg='#4D4744')


root.bind('w',lambda x: tecla_mover('w',jogo_atual))
root.bind('a',lambda x: tecla_mover('a',jogo_atual))
root.bind('s',lambda x: tecla_mover('s',jogo_atual))
root.bind('d',lambda x: tecla_mover('d',jogo_atual))



b00 = Frame(root,bg=('#938780'),height=100,width=100)
b00.grid(column=0,row=0,padx=7,pady=7)
b01 = Frame(root,bg=('#938780'),height=100,width=100)
b01.grid(column=1,row=0,padx=7,pady=7)
b02 = Frame(root,bg=('#938780'),height=100,width=100)
b02.grid(column=2,row=0,padx=7,pady=7)
b03 = Frame(root,bg=('#938780'),height=100,width=100)
b03.grid(column=3,row=0,padx=7,pady=7)
b10 = Frame(root,bg=('#938780'),height=100,width=100)
b10.grid(column=0,row=1,padx=7,pady=7)
b11 = Frame(root,bg=('#938780'),height=100,width=100)
b11.grid(column=1,row=1,padx=7,pady=7)
b12 = Frame(root,bg=('#938780'),height=100,width=100)
b12.grid(column=2,row=1,padx=7,pady=7)
b13 = Frame(root,bg=('#938780'),height=100,width=100)
b13.grid(column=3,row=1,padx=7,pady=7)
b20 = Frame(root,bg=('#938780'),height=100,width=100)
b20.grid(column=0,row=2,padx=7,pady=7)
b21 = Frame(root,bg=('#938780'),height=100,width=100)
b21.grid(column=1,row=2,padx=7,pady=7)
b22 = Frame(root,bg=('#938780'),height=100,width=100)
b22.grid(column=2,row=2,padx=7,pady=7)
b23 = Frame(root,bg=('#938780'),height=100,width=100)
b23.grid(column=3,row=2,padx=7,pady=7)
b30 = Frame(root,bg=('#938780'),height=100,width=100)
b30.grid(column=0,row=3,padx=7,pady=7)
b31 = Frame(root,bg=('#938780'),height=100,width=100)
b31.grid(column=1,row=3,padx=7,pady=7)
b32 = Frame(root,bg=('#938780'),height=100,width=100)
b32.grid(column=2,row=3,padx=7,pady=7)
b33 = Frame(root,bg=('#938780'),height=100,width=100)
b33.grid(column=3,row=3,padx=7,pady=7)

display(jogo_atual)
    # Label(root,text='Voce perdeu =(',bg='black',fg='white',font=40,height=25,width=50).grid(columnspan=4,rowspan=4,column=0,row=0)



root.mainloop()

