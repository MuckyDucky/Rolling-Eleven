import pygame
import sys
import time
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *

pygame.init()

cSec=0
cFrame=0
FPS=0

game_title="FIFAL Fantasy"




fps_font=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",20)
msg_font=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)#dont assume font exists. change later

sky = pygame.image.load("graphics\\sky.png")
Sky=pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))


del sky

def show_fps():
    fps_overlay=fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay,(0,0))

def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height=800,600
    window_title=game_title
    pygame.display.set_caption(window_title)
    window=pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_fps():
    global cSec, cFrame, FPS, deltatime
    
    if cSec==time.strftime("%S"):
        cFrame+=1
    else:
        FPS=cFrame
        cFrame = 0
        cSec=time.strftime("%S")
        if FPS > 0:
            deltatime=1 / FPS

def message_display(msg):
    text=msg_font.render(msg, True, Color.Red)
    text_rect=text.get_rect(center=(window_width/2, window_height/2))
    
    window.blit(text,text_rect)

#EVENTS LOOP
def main_loop():
    isRunning=True    
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                

            if event.type == pygame.KEYDOWN: #if key pressed
                if event.key == pygame.K_w:
                    Globals.camera_move=1
                elif event.key == pygame.K_s:
                    Globals.camera_move=2
                elif event.key == pygame.K_a:
                    Globals.camera_move=3
                elif event.key == pygame.K_d:
                    Globals.camera_move=4
                    
            elif event.type == pygame.KEYUP:
                Globals.camera_move=0
                    
                    
                

        #LOGIC
        if Globals.camera_move==1:
            Globals.camera_y += 100 * deltatime
        elif Globals.camera_move == 2:
            Globals.camera_y -= 100 * deltatime
        elif Globals.camera_move == 3:
            Globals.camera_x += 100 * deltatime
        elif Globals.camera_move == 4:
            Globals.camera_x -= 100 * deltatime         

            

        
        # RENDER GRAPHICS          
        window.blit(Sky, (0,0))

        #-Render Simple Grid
        for x in range (0,window_width, Tiles.Size):
            for y in range(0, window_height, Tiles.Size):
                window.blit(Tiles.Grass,(x,y))
        

        
        show_fps()
        
        pygame.display.update()

        count_fps()
    pygame.quit()
    sys.exit()    


        
def game_intro ():
    intro = True
    window.fill(Color.White)
    message_display('Welcome to '+game_title+'.\n Press Space to start game')
    pygame.display.update()
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro=False                    
                    main_loop()
                    
                            
                            
        
    
    
            
    

create_window()
game_intro()





        
        

        
        




    
