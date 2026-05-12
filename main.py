import pygame
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((1920, 1080 ))

noir = pygame.image.load("assets/carre noir.jpg").convert()
fond = pygame.image.load("assets/Dungeon.jpg").convert() # taille de l image 1200, 675
perso = pygame.image.load("assets/ours.png").convert_alpha() #taille de l image 400, 366
ennemi = pygame.image.load("assets/Superpingouin.png").convert_alpha() #taille de l image 250, 250
slot = pygame.image.load("assets/carre.png").convert_alpha() #taille de l image 60, 60
item = pygame.image.load("assets/epee.png").convert_alpha() # taille de l image 45, 45
main = pygame.image.load("assets/epee_grand.png").convert_alpha()
secret = pygame.image.load("assets/Marchand.png").convert_alpha()
sell = pygame.image.load("assets/galerie.png").convert_alpha() #taille de l image
poudre = pygame.image.load("assets/Blanc.png").convert_alpha()
menu_c = pygame.image.load("assets/losange_c.png").convert_alpha()
menu_a = pygame.image.load("assets/losange_a.png").convert_alpha()
menu_b = pygame.image.load("assets/losange_b.png").convert_alpha()
menu_r = pygame.image.load("assets/losange_r.png").convert_alpha()
light = pygame.image.load("assets/Light.png").convert_alpha()
gabe = pygame.image.load("assets/gabe.webp").convert_alpha()

fontGoth = pygame.font.Font('ManuskriptGotisch.ttf', 100)

running = True

slot_liste = [60, 140, 220, 300]
marchand = False
gabe_n = False
br = 0
marque = 0
running = True
#dictionaire des objets present dans le jeux organiser comme sa :
#[prix, description, sur quoi sa influe (pv, nombre de des...), nombre du changement de valeur, nom de l image, 1 si un anneau 0 sinon]
objet = {"poudre_i": [50, "Une poudre mysterieuse conferant de grand pouvoir", "pv", 30, poudre, 0]}

def font():
        fenetre.blit(secret, (450, 180))
        fenetre.blit(sell, (250, 525))    
        fenetre.blit(sell, (500, 525))    
        fenetre.blit(sell, (750, 525))
        fenetre.blit(poudre,(300, 625))

def utiliser(nom):
    if "pv" == objet[nom][2]:
        gamer.pv += objet[nom][3]
    if "nbr_d" == objet[nom][2]:
        gamer.nbr_d += objet[nom][3]

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
    
def lanceD(Ds:list) -> list:
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
        self.defense = randint(10, 15)
        
        #init sac a d
        d1 = D(6)
        d2 = D(6)
        self.sac_a_d[d1.name] = d1.liste_faces
        self.sac_a_d[d2.name] = d1.liste_faces

    def ajout_D(self, d):
        self.sac_a_d[d.name] = d.liste_faces

    def __repr__(self):
        return f'Pv: {self.pv}, Sac: {self.sac_a_d}'

class Monstre():
    
    def __init__(self, pv, atq, defense):
        self.pv = pv
        self.atq = atq
        self.etat = None
        self.defense = defense # pour comparaison: joueur a defense entre 10 et 15
    

class D():
    
    def __init__(self, nbr_faces, liste_faces=None, name='default'):
        self.nbr_faces = nbr_faces
        self.name = name
        self.pipé = False
        if liste_faces == None: # si liste de faces non déclaré, creer dé a x nombre de faces
            self.liste_faces = [i for i in range(nbr_faces)]
            self.name = f'D{self.nbr_faces}'
        else: # sinon liste de faces = liste de faces déclarées
            self.liste_faces = liste_faces                 
        
    def __repr__(self):
        return f'{self.name}'
    
    def print_faces(self):
        print(f'nom: {self.name}')
        print(f'indices: { [i for i in range(self.nbr_faces)] }')
        print(f'faces:   {self.liste_faces}')
                           
    def set_faces(self, indice, face):
        self.liste_faces[indice] = face
    
    def roll(self):
        return self.liste_faces[randint(0, self.nbr_faces - 1)]
        
    def pipé(self):
        self.pipé = True
        #todo
        

def attaque(auteur, cible):
    return sum(lanceD(auteur.sac_a_d))
    

def sysCombat(player, liste_ennemies): #args: joueur, liste des objets de type ennmies
    # entity = [i+1 for i in range(liste_ennemies+1)]
    liste_entites = [player] + liste_ennemies
    ordre_tour = sorted(liste_entites, key=lambda x:x.vitesse)
    
    gagne = None
    combatRunning = True
    indiceActif = 0
    nombreMort = 0
    
    while combatRunning:
        actif = ordre_tour[indiceActif]
        print(f"C'est au tour de {actif.name}")
        
        #choix bouton
        
        for i in liste_entites:
            if i.pv == 0:
                nombreMort +=1
                
        if nombreMort == len(liste_ennemies):
            # victoire joueur
            print('Combat gagné')
            gagne = True
            combatRunning = False
            
        elif player.pv == 0:
            # defaite joueur
            print('Combat perdu')
            gagne = False
            combatRunning = False
            
        else:
            indiceActif +=1
            # tour suivant
    
    # sorti du combat ->
    return gagne # return True si combat gagné,
    
    
#                     pv atq  def
tux =         Monstre(40, 20, 15)
angry_tux =   Monstre(45, 40, 10)
machete_tux = Monstre(40, 50, 10)

linus =       Monstre(300, 70, 20)
angry_linus = Monstre(300, 100, 20)
dark_linus =  Monstre(1000, 200, 100) # boss final (impossible)

while running:
    pygame.display.update()
    
    # main code
    
    keys = pygame.key.get_pressed()
    fenetre.blit(noir, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fenetre.blit(fond, (100,0))

    if marchand == True:
        font()
    
    elif gabe_n == True:
        fenetre.blit(gabe, (500, 180))
    
    else:
        if br > 100:
            fenetre.blit(perso, (150,310))
            br += 1
        elif br <= 100:
            fenetre.blit(perso, (150,313))
            br += 1
        if br == 200:
            br = 0
        
        fenetre.blit(ennemi, (750,280))
        fenetre.blit(main, (360,480))
        fenetre.blit(menu_r, (500,650))
        fenetre.blit(menu_a, (375,550))
        fenetre.blit(menu_b, (625,550))
        fenetre.blit(menu_c, (500,450))
        
        if marque == 0 : 
            fenetre.blit(light, (500,450))
        if marque == 1 : 
            fenetre.blit(light, (375,550))     
        if marque == 2 : 
            fenetre.blit(light, (625,550))
        if marque == 3 : 
            fenetre.blit(light, (500,650))      
        
        if keys[pygame.K_UP]:
            marque = 0
        
        if keys[pygame.K_LEFT]:
            marque = 1
        
        if keys[pygame.K_RIGHT]:
            marque = 2
            
        if keys[pygame.K_DOWN]:
            marque = 3     
            
    for c in slot_liste:
        fenetre.blit(slot, (25,c))
    
    if keys[pygame.K_m]:
        marchand = True
        gabe_n = False
    
    if keys[pygame.K_l]:
        marchand = False
        gabe_n = False

    if keys[pygame.K_g]:
        gabe_n = True
        marchand = False
    
      
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
