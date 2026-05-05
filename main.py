import pygame
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((1920, 1080 ))
fontGoth = pygame.font.Font('ManuskriptGotisch.ttf', 100)

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
    
def lanceD(Ds:list):
    res = []
    for i in Ds:
        res.append(i.roll())
    return res
        

class Joueur():
    
    def __init__(self):
        self.pv = 100
        self.nbr_d = 2
        self.etat = None
        self.doigts = 10
        self.bagues = 0
        self.sac_a_d = {}
        
        #init sac a d
        d1 = D(6)
        d2 = D(6)
        self.sac_a_d[d1.name] = d1.liste_faces
        self.sac_a_d[d2.name] = d1.liste_faces

        
        
class Monstre():
    
    def __init__(self, pv, atq, vitesse):
        self.pv = pv
        self.atq = atq
        self.etat = None
        self.vitesse = vitesse
    
class D():
    
    def __init__(self, nbr_faces, liste_faces=None, name='default'):
        self.nbr_faces = nbr_faces
        self.name = name
        self.pipé = False
        if liste_faces == None: # si liste de faces non déclaré, creer dé a x nombre de faces
            self.liste_faces = [i for i in range(nbr_faces)]
        else: # sinon liste de faces = liste de faces déclarées
            self.liste_faces = liste_faces                 
        
    def __repr__(self):
        return f'{self.name}'
    
    def print_faces(self):
        print(f'nom: {self.name}')
        print(f'indices: {[i for i in range(self.nbr_faces)]}')
        print(f'faces:   {self.liste_faces}')
                           
    def set_faces(self, indice, face):
        self.liste_faces[indice] = face
    
    def roll(self):
        return self.liste_faces[randint(0, self.nbr_faces - 1)]
        
    def pipé(self):
        self.pipé = True
        

sac = [D(randint(4,10)) for i in range(5)]
print(sac)
print(lanceD(sac))

a = Joueur()

print(a.sac_a_d)

while running:
 
 
 
    pygame.display.update()    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
