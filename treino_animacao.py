from tkinter import *
import time

config_path = 'C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\Programaçao\\Projetos\\arquivos\\teste_animacao_config.txt'
with open(config_path,'r') as config:
    content = config.read()
read = 0
content2 = ''
configuracao = []
for i in content:
    if i == '=':
        read = 1
        continue
    if i == '\n':
        configuracao.append(int(content2))
        content2 = ''
        read = 0
        continue
    if read == 1:
        content2 += i

HEIGHT = configuracao[0]
WIDTH = configuracao[1]
xdeslocamento = configuracao[2]
ydeslocamento = configuracao[3]



root = Tk()
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

path_imagem_file = 'C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\Programaçao\\Projetos\\arquivos\\Zagreus_pequeno.png'
imagem_file = PhotoImage(file=path_imagem_file)
imagem = canvas.create_image(0,0,image= imagem_file, anchor= NW)

while True:
    canvas.move(imagem,xdeslocamento,ydeslocamento)
    cordenadas = canvas.coords(imagem)
    if cordenadas[0] > WIDTH - imagem_file.width() or cordenadas[0] < 0:
        xdeslocamento = -xdeslocamento
    if cordenadas[1] > HEIGHT - imagem_file.height() or cordenadas[1] < 0:
        ydeslocamento = -ydeslocamento
    root.update()
    time.sleep(0.01)



root.mainloop()