from tkinter import *
import random

class Snake():
    def __init__(self):
        self.coords = [[0, 0],[0, 0],[0, 0]]
        self.squares = []

        for x, y in self.coords:
            square = canvas.create_rectangle(x,y,x+30,y+30,fill='green',tag='snake')
            self.squares.append(square)

class Food():
    def __init__(self):
        x = random.randint(0, 23)*30
        y = random.randint(0, 23)*30
        self.coords = [x, y]  
        canvas.create_oval(x,y,x+30,y+30,fill='yellow',tag='food')      




def new_game():
    pass



def movimento(snake,food):
    
    x, y = snake.coords[0]

    if direction == 'up':
        y -= 30
    elif direction == 'down':
        y += 30
    elif direction == 'left':
        x -= 30
    elif direction == 'right':
        x += 30

    snake.coords.insert(0, [x, y])
    square = canvas.create_rectangle(x,y,x+30,y+30,fill='green')
    snake.squares.insert(0, square)
    
    if x == food.coords[0] and y == food.coords[1]:
        canvas.delete('food')
        del food
        food = Food()
        global pontos
        pontos += 1
        root.title('Cobrinha                Pontos = {}'.format(pontos))
    else:
        del snake.coords[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if colisao(snake) == True:
        print('perdeu')
    else:
        canvas.after(80,movimento,snake,food)



def change_direction(new_direction):
    global direction

    if new_direction == 'up' and direction != 'down':
        direction = 'up'
    if new_direction == 'down' and direction != 'up':
        direction = 'down'
    if new_direction == 'right' and direction != 'left':
        direction = 'right'
    if new_direction == 'left' and direction != 'right':
        direction = 'left'



def colisao(snake):
    x, y = snake.coords[0]

    if x < 0 or x >= 720:
        return True
    if y < 0 or y >= 720:
        return True
    
    for i in snake.coords[1:]:
        if x == i[0] and y == i[1]:
            return True
    return False

pontos = 0
root = Tk()
root.title('Cobrinha                Pontos = {}'.format(pontos))


canvas = Canvas(root,height=720,width=720,bg='black')
canvas.pack()

root.geometry('720x720+430+50')

root.bind('<Up>', lambda x: change_direction('up'))
root.bind('<Down>', lambda x: change_direction('down'))
root.bind('<Left>', lambda x: change_direction('left'))
root.bind('<Right>', lambda x: change_direction('right'))


snake = Snake()
food = Food()

direction = 'down'

movimento(snake, food)

root.mainloop()