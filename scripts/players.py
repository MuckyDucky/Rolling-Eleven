import pygame
import random

class Player:
    def __init__(self, name,turn):
        self.name=name
        self.money=400
        self.turn=turn
        
        self.score=0
        self.roster=[]
        self.diceVal=0
        self.avgAtk=0
        self.avgDfns=0
        self.avgStm=0
        self.totalPwr=0
                
    def score_goal(self):
        self.score+=1
    def add_to_roster(self,athlete):
        self.roster.append(athlete) #fix later
    def assignDiceVal(self,diceval):
        self.diceVal=diceval
    def updateAvgs(self):
        print('updating Avgs')
        rosterLen=len(self.roster)
        if rosterLen:
            totalAtk=0
            totalDfns=0
            totalStm=0
            for ath in self.roster:
                totalAtk+=ath.atk
                totalDfns+=ath.dfns
                totalStm+=ath.stm
            self.avgAtk=totalAtk/rosterLen
            self.avgDfns=totalDfns/rosterLen
            self.avgStm=totalAtk/rosterLen
            
    def buy_athlete(self,athlete):
        if self.money>=athlete.price and len(self.roster)<4:
            self.money-=athlete.price
            self.add_to_roster(athlete)
            self.updateAvgs()
    def rollDice(self):
        self.diceVal=random.randrange(1,7)
        print(self.diceVal)
        return self.diceVal


class Athlete:
    def __init__(self, name, pos, atk, dfns, stm, price):
        self.name=name
        self.pos=pos
        self.atk=atk
        self.dfns=dfns
        self.stm=stm
        self.price=price
    def reduceStm(num):
        self.stm-=num
    bpos_x=0
    bpos_y=0

def make_athlete(name,pos,atk,dfns,stm,price):
    athlete=Athlete(name,pos,atk,dfns,stm,price)
    return athlete

def make_player(name,turn):
    player=Player(name,turn)
    
    return player


players=[]
players.append(make_player('Player 1',True))
players.append(make_player('Player 2',False))

athletes=[]

athletes.append(make_athlete('Messi', 'FW', 10,4,5,120))
athletes.append(make_athlete('Ronaldo', 'FW', 10,3,7,120))
athletes.append(make_athlete('Suarez', 'FW', 9,3,7,100))
athletes.append(make_athlete('Neymar', 'FW', 10,2,7,100))
athletes.append(make_athlete('Salah', 'FW', 8,4,8,90))
athletes.append(make_athlete('Hazard', 'FW', 9,3,6,90))
athletes.append(make_athlete('H.M. Son', 'FW', 7,5,7,60))
athletes.append(make_athlete('De Bruyne', 'MF', 7,6,5,80))
athletes.append(make_athlete('Pogba', 'MF', 7,5,6,80))
athletes.append(make_athlete('Kante', 'MF', 5,8,5,70))
athletes.append(make_athlete('Kroos', 'MF', 7,6,6,90))
athletes.append(make_athlete('D.Silva', 'MF', 8,4,4,80))
athletes.append(make_athlete('Busquets', 'MF', 5,7,5,80))
athletes.append(make_athlete('Modric', 'MF', 7,5,4,80))
athletes.append(make_athlete('Ramos', 'DF', 3,9,8,80))
athletes.append(make_athlete('Pique', 'DF', 4,8,7,70))
athletes.append(make_athlete('Hummels', 'DF', 4,10,5,90))
athletes.append(make_athlete('Chiellini', 'DF', 3,10,5,80))
athletes.append(make_athlete('De Gea', 'GK', 2,8,5,80))
athletes.append(make_athlete('Neuer', 'GK', 3,9,3,90))
athletes.append(make_athlete('Courtois', 'GK', 2,9,5,70))

        
            
        
        
