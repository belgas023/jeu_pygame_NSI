import pygame
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((1920, 1080 ))

running = True

etat = [
        'menu-depart', # menu principal
        'combat', 
        'maison', # amelioration des dés
        'jardin'  # upgrades permanentes joueur 
        ]
etat_actuel = etat[0]
def changerEtat(a): # changer l'etat actuel par a
    global etat_actuel
    etat_actuel = etat[etat.index(a)]




def sysCombat(player, ennemy):
    pass
    

class Joueur():
    
    def __init__(self):
        self.pv = 100
        self.nbr_d = 2
        self.etat = None
        self.doigts = 10
        self.bagues = 0
        
        
class Monstre():
    
    def __init__(self, pv, atq, vitesse):
        self.pv = pv
        self.atq = atq
        self.etat = None
        self.vitesse = vitesse
    
class D():
    
    def __init__(self, nbr_nfaces):
        self.nbr_faces = nbr_faces
        self.pipé = False
        
        
    def pipé(self):
        self.pipé = True
        
        
        
        
                 
                 
                                 
while running:
    
    
    
    
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
