import pygame,random
from  pygame.locals import *
import time
from os import path
import shelve
import os

SIZE=40
class Obstacle:
    def __init__(self,parent_screen):
        self.img=pygame.image.load("resources/obs.jpg").convert()
        self.parent_screen=parent_screen
        self.x=[80,120,160,200,880,920,960,520]
        self.y=[120,40,120,520,560,400,440,80]

    
    


    def draw(self):
       
      
        for i in range (8):
          self.parent_screen.blit(self.img,(self.x[i],self.y[i])) #its show the block on the position
        pygame.display.flip() #its update the things that we add to the serfuce      

class Orange:
    def __init__(self,parent_screen):
        self.image=pygame.image.load("resources/orange.png").convert()
        self.parent_screen=parent_screen
        self.x=SIZE*12
        self.y=SIZE*12

    def draw(self):
        
        self.parent_screen.blit(self.image,(self.x,self.y)) 
        pygame.display.flip() 
    def move(self):
        self.x=random.randint(15,21)*SIZE
        self.y=random.randint(3,14)*SIZE  

            
 

class Strawberry:
    def __init__(self,parent_screen):
        self.image=pygame.image.load("resources/strawberry.png").convert()
        self.parent_screen=parent_screen
        self.x=SIZE*8
        self.y=SIZE*8

    def draw(self):
        
        self.parent_screen.blit(self.image,(self.x,self.y)) 
        pygame.display.flip() 
    def move(self):
        self.x=random.randint(10,15)*SIZE
        self.y=random.randint(8,14)*SIZE  



class Apple:
    def __init__(self,parent_screen):
        self.image=pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen=parent_screen
        self.x=SIZE*3
        self.y=SIZE*3

    def draw(self):
        #self.parent_screen.fill((0,0,0)) 
        self.parent_screen.blit(self.image,(self.x,self.y)) #its show the block on the position
        pygame.display.flip() #its update the things that we add to the serfuce
    def move(self):
        self.x=random.randint(6,10)*SIZE
        self.y=random.randint(3,14)*SIZE        
   



class Snake:
    def __init__(self,parent_screen,length):
       self.lenght=length 
       self.parent_screen=parent_screen
       self.block=pygame.image.load("resources/snake.jpg").convert()
       self.x=[SIZE]*length
       self.y=[SIZE]*length
       self.direction='down'



    def increase_lenght(self):
        self.lenght+=1

        self.x.append(-1)
        
        self.y.append(-1)

   
    def move_left(self):
        self.direction='left'

    def move_right(self):
        self.direction='right'
    def move_up(self):
        self.direction='up' 
    def move_down(self):
          self.direction='down'

    def walk(self):

        for i in range (self.lenght-1,0,-1):
            self.x[i]=self.x[i-1] #the currunt x position will previuos x postion 
            self.y[i]=self.y[i-1]

        if self.direction=='up':
            self.y[0] -=SIZE #its increase depend on block
        if self.direction=='down':
            self.y[0] +=SIZE
        if self.direction=='right':
            self.x[0] +=SIZE
        if self.direction=='left':
            self.x[0] -=SIZE

        self.draw()     
    def draw(self):
        self.parent_screen.fill((52, 235, 76)) 
        for i in range (self.lenght):
          self.parent_screen.blit(self.block,(self.x[i],self.y[i])) #its show the block on the position
        pygame.display.flip() #its update the things that we add to the serfuce      





        



class Game:
    

    def __init__(self) :
        pygame.init()
        
        self.surface=pygame.display.set_mode((1000,600))# is intitaling game window
        self.highscore=0
        self.score=0
        self.surface.fill((52, 235, 76)) 
        self.snake=Snake(self.surface,1)
        self.strawberry=Strawberry(self.surface)
        self.apple=Apple(self.surface) 
        self.obstacle=Obstacle(self.surface)
        self.orange=Orange(self.surface)
        
      
       
        


    def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1<x2+SIZE:
            if y1>=y2 and y1<y2+SIZE:
                return True
              

        return False   
          

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.strawberry.draw()
        self.obstacle.draw()
        self.orange.draw()
        self.display_score()
        self.changehighscore()
        self.display_highscore()
       
      
        pygame.display.flip()

        #snake collidig with applle
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.score+=1
            self.snake.increase_lenght()
            self.apple.move()
        #snake colliding with strawberry:
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.strawberry.x,self.strawberry.y):
            self.score+=3
            self.snake.increase_lenght()
            self.strawberry.move()
          #snake colliding with orange:   
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.orange.x,self.orange.y):
            self.score+=5

            self.snake.increase_lenght()
            self.orange.move()    

        #snake collidig wiht itself

        for i in range(3,self.snake.lenght):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise " Game over"

        #snake collidig with walls
        if self.snake.x[0]<0 or self.snake.y[0]<0 or self.snake.x[0]>1000 or self.snake.y[0]>600:

            raise " Game over"
        
       #snake collding with obstacle
        for i in range(0,8):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.obstacle.x[i],self.obstacle.y[i]):
                raise " Game over"

    
    def display_score(self):

        font=pygame.font.SysFont('arial',30)
        score=font.render(f"Score:{self.score}",True,(23, 3, 252))
        self.surface.blit(score,(900,10))

    def changehighscore(self):
        if self.score>self.highscore:
             self.highscore=self.score


    def display_highscore(self):
        
        font=pygame.font.SysFont('arial',30)
        hsiscorr =font.render(f"High Score:{self.highscore}",True,(23, 3, 252))
        self.surface.blit(hsiscorr,(10,10))
    
    
    def show_game_over(self):
        self.surface.fill((52, 235, 76))
        font=pygame.font.SysFont('arial',30)
        line1=font.render(f"Your final is Score : {self.score}",True,(23, 3, 252))
        self.surface.blit(line1,(250,300))
        line2=font.render("To play again press Enter",True,(23, 3, 252))
        self.surface.blit(line2,(250,350))
        
        pygame.display.flip()
        
       
    def reset(self):
        self.snake=Snake(self.surface,1)# because we have snake in our game
        self.apple=Apple(self.surface)
        self.score=0 

    def run(self):
      pause=False
      running=True
      #event loop
      while running:
        for event in pygame.event.get():
            if event.type==KEYDOWN:

                if event.key==K_ESCAPE:      # for exit the program
                    running==False
                if event.key==K_RETURN:
                    pause=False
                if not pause:
                   if event.key==K_UP:
                     self.snake.move_up() 
                   if event.key==K_DOWN:
                     self.snake.move_down()   
                   if event.key==K_LEFT:
                     self.snake.move_left()
                   if event.key==K_RIGHT:
                     self.snake.move_right()

            elif event.type==QUIT:
                 running=False
        try:
            if not pause:
               self.play()  

        except Exception as e:

            self.show_game_over() 
            pause=True 
            self.reset()       

        time.sleep(0.3)       
   

if __name__=="__main__":
    game=Game()
    game.run()

   




    






