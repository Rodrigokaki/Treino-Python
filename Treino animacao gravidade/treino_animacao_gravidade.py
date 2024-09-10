from tkinter import *
import time
from logica_gravidade import *
import threading

HEIGHT = 700
WIDTH = 1000
GRAVIDADE = 10


root = Tk()
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bola_teste = Bola(canvas, 475, 150, 50,'red', 1.6, 0.8)
bola_2 = Bola(canvas, 100,100, 75,'pink',GRAVIDADE, 0.9)
bola_felipe = Bola(canvas, 250,100, 60, 'black',GRAVIDADE,0.6)
bola_kaki = Bola(canvas, 700, 500, 100,'green',GRAVIDADE,1.0)

bola1 = threading.Thread(target=bola_teste.cair,daemon=True)
bola2 = threading.Thread(target=bola_2.cair,daemon=True)
bola3 = threading.Thread(target=bola_felipe.cair,daemon=True)
bola4 = threading.Thread(target=bola_kaki.cair,daemon=True)

bola1.start()
bola2.start()
bola3.start()
bola4.start()


root.mainloop()