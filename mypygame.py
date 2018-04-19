import pygame
import sys
import time
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *
from scripts.players import *



pygame.init()

cSec=0
cFrame=0
FPS=0

game_title="FIFAL Fantasy"

clicked=False



fps_font=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",20)
msg_font=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)#dont assume font exists. change later
main_font=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 15)
pck_font=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",20)

sky = pygame.image.load("graphics\\sky.png")
Sky=pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))

interact=None
buttons=[]

del sky

def getFont(name = "Courier New", size = 20, style = ''):           #POST: Returns the font the Caller wants
    return pygame.font.SysFont(name, size, style)

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

def text_objects(text, font):
    textsurface = font.render(text,True,Color.Black)
    return textsurface, textsurface.get_rect()

##def display_stats(athlete):
##    #show stats
##    nameText=main_font.render(athlete.name,True,Color.Yellow)
##    nameText_rect=nameText.get_rect(center=(window_width/2, window_height/2-40))
##    priceText=main_font.render('$'+str(athlete.price),True,Color.Yellow)
##    priceText_rect=priceText.get_rect(center=(window_width/2, window_height/2-20))
##    statsText=main_font.render('ATK: ' + str(athlete.atk) + ' DEF: ' + str(athlete.dfns) + ' STM : ' + str(athlete.stm),True,Color.Yellow)
##    statsText_rect=statsText.get_rect(center=(window_width/2, window_height/2))
##    
##
##    mouse = pygame.mouse.get_pos()
##    if athlete.bpos_x<mouse[0]<athlete.bpos_x+100 and athlete.bpos_y<mouse[1]<athlete.bpos_y+50:
##        window.blit(nameText,nameText_rect)
##        window.blit(priceText,priceText_rect)
##        window.blit(statsText,statsText_rect)

def display_player_roster():
    
    name1Text=main_font.render(players[0].name + ' ' + str(players[0].money) + 'G remaining' ,True,Color.Yellow)
    name1Text_rect=name1Text.get_rect(center=(window_width/4, 3*window_height/4))
    
    name2Text=main_font.render(players[1].name  + ' ' + str(players[1].money) + 'G remaining' ,True,Color.Yellow)
    name2Text_rect=name2Text.get_rect(center=(3*window_width/4, 3*window_height/4))

    p1roster="Roster: "
    p2roster="Roster: "

    
    
    for ath in players[0].roster:
        p1roster+=ath.name + ', '
        
    for ath in players[1].roster:
        p2roster+=ath.name + ', '

    roster1Text= main_font.render(p1roster,True,Color.Yellow)
    roster1Text_rect= roster1Text.get_rect(center=(window_width/4, 3*window_height/4+20))

    roster2Text= main_font.render(p2roster,True,Color.Yellow)
    roster2Text_rect= roster2Text.get_rect(center=(3*window_width/4, 3*window_height/4+20))


    pckmsg=", select a player to buy"
    pckText=None
    pckText_rect=None

    
    if players[0].turn:
        pygame.draw.rect(window, Color.Red, [80, 5*window_height/8+40, 250, 100], 2)
        pckText=pck_font.render(players[0].name+pckmsg,True,Color.Red)
        pckText_rect=pckText.get_rect(center=(window_width/4, 3*window_height/4-60))
    elif players[1].turn:
        pygame.draw.rect(window, Color.Red, [window_width/2+80, 5*window_height/8+40, 250, 100], 2)
        pckText=pck_font.render(players[1].name+pckmsg,True,Color.Red)
        pckText_rect=pckText.get_rect(center=(3*window_width/4, 3*window_height/4-60))
        
    
    window.blit(name1Text,name1Text_rect)
    window.blit(name2Text,name2Text_rect)
    window.blit(roster1Text,roster1Text_rect)
    window.blit(roster2Text,roster2Text_rect)
    window.blit(pckText,pckText_rect)

def display_battle_status():
    pygame.draw.line(window, Color.White, (window_width/2,0),(window_width/2,window_height))
    pygame.draw.circle(window, Color.White, (int(window_width/2), int(window_height/2)),50,2)
    #pygame.draw.rect(window, Color.Red, [80, 5*window_height/8+40, 250, 100], 2)
    pygame.draw.rect(window, Color.White, [0, window_height/4, window_width/6 , window_height/2],2)
    pygame.draw.rect(window, Color.White, [window_width-window_width/6, window_height/4, window_width/6 , window_height/2],2)
                                           
    
    name1Text=main_font.render(players[0].name,True,Color.Yellow)
    name1Text_rect=name1Text.get_rect(center=(window_width/4, 3*window_height/4))
    
    name2Text=main_font.render(players[1].name,True,Color.Yellow)
    name2Text_rect=name2Text.get_rect(center=(3*window_width/4, 3*window_height/4))


    window.blit(name1Text,name1Text_rect)
    window.blit(name2Text,name2Text_rect)
        

class ClickableRect():
    def __init__(self, pos, size):
        self.rect=pygame.Rect((0,0),size)
        self.rect.center=pos

        self.hasClicked=False
    def isMouseOver(self):
        cur = pygame.mouse.get_pos()

        if self.rect.left<cur[0]<self.rect.right and self.rect.top<cur[1]<self.rect.bottom:
            return True
        else:
            return False

    def doMouseOver(self):
        #print('You moused over a rect')
        pass

    def isLeftMouseDown(self): ##
        return self.hasClicked

    def doLeftMouseDown(self): #when left mouse held down
        pass
        
    def isClicked(self):
        global interact
        mouse = pygame.mouse.get_pressed()

        if self.isMouseOver():
            if mouse[0] and self.hasClicked==False and not interact:
                self.hasClicked=True #left mouse button currently down
                interact=self
                return True
        if mouse[0] == False and self.hasClicked==True: #if left mouse goes up
            self.hasClicked==False
            interact = None

        return False    

    def doClick(self):
        print('You Clicked a Rect')
        

    def update(self, window):
        if self.isMouseOver():
            self.doMouseOver()

        if self.isLeftMouseDown():
            self.doLeftMouseDown()
                
        if self.isClicked():
            self.doClick()


class Button(ClickableRect):
    def __init__(self,pos,size,color):
        ClickableRect.__init__(self, pos, size)
        
        self.color = color
        self.image=pygame.Surface(size)
        self.image.fill(self.color)
        

    def doMouseOver(self):
        overlay = pygame.Surface(self.rect.size)
        overlay.set_alpha(60)
        overlay.fill(Color.Black)
        self.image.blit(overlay, (0,0))

    def doLeftMouseDown(self):
        self.image.fill(Color.Green)
        
    def doClick(self): #click action for single frame
        print('You clicked a button')
        
        
    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self, window):
        self.image.fill(self.color)
        

        ClickableRect.update(self,window)
        self.draw(window)

class TextButton(Button):
    def __init__(self,pos,size,color,text):
        Button.__init__(self, pos, size, color)
        self.text=getFont(size=36, style='bold').render(text,True,Color.Black)

    def draw(self, window):
        self.image.blit(self.text, (10,10))
        Button.draw(self,window)

class MarketButton(TextButton):
    def __init__(self, pos, size, color, text, athIdx):
        TextButton.__init__(self,pos,size,color,text)
        self.athIdx=athIdx

    def doClick(self):
        if phs.phase=='pick':
            nextTurnIdx=None
            for idx,p in enumerate(players):
                if p.turn==True:
                    p.buy_athlete(athletes[self.athIdx])
                    p.turn=False
                    if idx==0:
                        nextTurnIdx=1
                    elif idx==1:
                        nextTurnIdx=0
            players[nextTurnIdx].turn=True

            if len(players[0].roster)==4 and len(players[1].roster)==4:
                print('both rosters are full')
                
                phs.phase='ready'
                print(phs.phase)

    def display_stats(self):
        nameText=main_font.render(athletes[self.athIdx].name,True,Color.Yellow)
        nameText_rect=nameText.get_rect(center=(window_width/2, window_height/2-40))
        priceText=main_font.render('$'+str(athletes[self.athIdx].price),True,Color.Yellow)
        priceText_rect=priceText.get_rect(center=(window_width/2, window_height/2-20))
        statsText=main_font.render('ATK: ' + str(athletes[self.athIdx].atk) + ' DEF: ' + str(athletes[self.athIdx].dfns) + ' STM : ' + str(athletes[self.athIdx].stm),True,Color.Yellow)
        statsText_rect=statsText.get_rect(center=(window_width/2, window_height/2))
        window.blit(nameText,nameText_rect)
        window.blit(priceText,priceText_rect)
        window.blit(statsText,statsText_rect)
                

    def doMouseOver(self):
        if phs.phase=='pick':
        
            overlay = pygame.Surface(self.rect.size)
            overlay.set_alpha(60)
            overlay.fill(Color.Black)
            self.image.blit(overlay, (0,0))
            self.display_stats()
        

        
    def update(self, window):
        self.image.fill(self.color)
        
        ClickableRect.update(self,window)
        self.draw(window)

class ReadyButton(TextButton):
    def __init__(self,pos,size,color,text):
        TextButton.__init__(self,pos,size,color,text)
        
    def doClick(self):
        phs.phase='battle'

    def update(self, window):
        if phs.phase=='ready': 
            self.image.fill(self.color)
            

            ClickableRect.update(self,window)
            self.draw(window)        
        
class Phase():
    def __init__(self, phase):
        self.phase=phase



    
    

def button(msg,x,y,w,h,iCol,aCol,athlete): #later loop over player names
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    
    
##     
##    if x < mouse[0] < x+w and y < mouse[1] < y+h:       
##        pygame.draw.rect(window, aCol, (x,y,w,h))
##        #print('mouse in button')
##        print(clicked)
##        #if clicked:
##        if click[0]: 
##            print('button clicked')
##            for p in players:
##                if p.turn==True:
##                    p.buy_athlete(athlete)
##            clicked=True
##            #print(click)
##                   
##        #else:
##            #print('not clicked')
##                    
##                    #p.buy_athlete(objAth.name)
##                
##                            
##                    #print(objAth.name)
##                    
##    else:            
##        pygame.draw.rect(window, iCol, (x,y,w,h))
##    smallText=main_font
    textSurf, textRect=text_objects(msg, smallText)
    textRect.center=((x+(w/2)),(y+(h/2))) #x,y
    window.blit(textSurf, textRect)

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

                
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                clicked=True
                print(clicked)
                
                
                    
                

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


### pick phase
        if(phs.phase=='pick' or phs.phase=='ready'):


            
            for mktButton in buttons:
                mktButton.update(window)
            
            rdyButton.update(window)
                         
            display_player_roster()


            pygame.display.update()

### battle phase            
        elif(phs.phase=='battle'):
            display_battle_status()

            
            pygame.display.update()
            

            
        show_fps()
        
        
        

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

            
#variables
#rect=ClickableRect((window.get_rect().centerx, window.get_rect().centery),(200,80))
#button=Button((window.get_rect().centerx, window.get_rect().centery),(200,80),Color.Red)
#txtButton=TextButton((window.get_rect().centerx,window.get_rect().centery + 100),(200,80), Color.Red, "Button3",0)
#mktButton=MarketButton((window.get_rect().centerx,window.get_rect().centery + 100),(200,80), Color.Red, "Button3",0)
rdyButton=ReadyButton((window.get_rect().centerx,window.get_rect().centery + 100),(200,80), Color.Red, "Click to start the match!")
for idx,item in enumerate(athletes):
            row = idx//7
            col = idx-row*7
            button=MarketButton((10+100*col,10+60*row),(100,50), Color.Blue, item.name, idx)
            buttons.append(button)
phs=Phase('pick')            
            
#def __init__(self, pos, size, color, text, athIdx):

game_intro()







        
        

        
        




    
