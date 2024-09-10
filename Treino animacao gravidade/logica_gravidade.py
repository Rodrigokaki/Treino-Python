import time
import math

class Bola:

    def __init__(self, canvas, x, y, diametro, cor, gravidade, elasticidade):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.diametro = diametro
        xdiametro = x + diametro
        ydiametro = y + diametro
        self.xdiametro = xdiametro
        self.image = canvas.create_oval(x,y,xdiametro,ydiametro,fill=cor)
        self.gravidade = gravidade
        self.elasticidade = elasticidade
        self.velocidade = 0


    def cair(self):
        while True:
            coordenadas = self.canvas.coords(self.image)
            if (coordenadas[3]+self.velocidade) >= (self.canvas.winfo_height()) and self.canvas.winfo_height() != 1:
                self.energia = (self.velocidade*self.velocidade)
                self.energia = self.energia*self.elasticidade
                self.velocidade = -math.sqrt(self.energia)
            else:
                self.canvas.move(self.image, 0, self.velocidade)
            self.velocidade += (self.gravidade*0.1)
            time.sleep(0.01)