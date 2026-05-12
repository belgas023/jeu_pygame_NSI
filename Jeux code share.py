import pygame

pygame.init()

fenetre = pygame.display.set_mode((1920, 1080 ))
noir = pygame.image.load("carre noir.jpg").convert()
fond = pygame.image.load("Dungeon.jpg").convert() # taille de l image 1200, 675
perso = pygame.image.load("ours.png").convert_alpha() #taille de l image 400, 366
ennemi = pygame.image.load("Superpingouin.png").convert_alpha() #taille de l image 250, 250
slot = pygame.image.load("carre.png").convert_alpha() #taille de l image 60, 60
item = pygame.image.load("epee.png").convert_alpha() # taille de l image 45, 45
main = pygame.image.load("epee_grand.png").convert_alpha()
secret = pygame.image.load("Marchand.png").convert_alpha()
sell = pygame.image.load("galerie.png").convert_alpha() #taille de l image
poudre = pygame.image.load("Blanc.png").convert_alpha()
menu_c = pygame.image.load("losange_c.png").convert_alpha()
menu_a = pygame.image.load("losange_a.png").convert_alpha()
menu_b = pygame.image.load("losange_b.png").convert_alpha()
menu_r = pygame.image.load("losange_r.png").convert_alpha()
light = pygame.image.load("Light.png").convert_alpha()
gabe = pygame.image.load("gabe.webp").convert_alpha()

slot_liste = [60, 140, 220, 300]
marchand = False
gabe_n = False
br = 0
marque = 0
running = True
#dictionaire des objets present dans le jeux organiser comme sa :
#[prix, description, sur quoi sa influe (pv, nombre de des...), nombre du changement de valeur, nom de l image, 1 si un anneau 0 sinon]
objet = {"poudre_i": [50, "Une poudre mysterieuse conferant de grand pouvoir", "pv", 30, poudre, 0]}




class Joueur():
    
    def __init__(self):
        self.pv = 100
        self.argent = 50
        self.nbr_d = 2
        self.etat = None
        self.doigts = 10
        self.bagues = 0

gamer = Joueur()

#class Item():
#    def initialiser(self, prix, description, utilite):
#        self.prix = prix
#        self.description = description
#        self.utilite = utilite
# A voir si utile        
        
def utiliser(nom):
    if "pv" == objet[nom][2]:
        gamer.pv += objet[nom][3]
    if "nbr_d" == objet[nom][2]:
        gamer.nbr_d += objet[nom][3]
        
utiliser("poudre_i")
print(gamer.pv)


def font():
        fenetre.blit(secret, (450, 180))
        fenetre.blit(sell, (250, 525))    
        fenetre.blit(sell, (500, 525))    
        fenetre.blit(sell, (750, 525))
        fenetre.blit(poudre,(300, 625))

while running:
    
    pygame.display.update()
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
        

pygame.quit()
