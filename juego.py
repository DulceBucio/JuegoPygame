from pygame import *
import sys, time

init() 
screen = display.set_mode((800,600)) 
pirateFont = font.Font("Pirate Ship.ttf", 20)
activo1 = False
velocity = 5
activo = 0


def Inicio(escena):
    global activo
    fondo1 = image.load("fondoinicio1.png")
    fondo1 = transform.scale(fondo1,(800,600))
    fondo2 = image.load("fondoinicio2.png")
    fondo2 = transform.scale(fondo2, (800, 500))
    nube1 = image.load("nube1.png")
    nube2 = image.load("nube2.png")
    nube3 = image.load("nube3.png")
    nube4 = image.load("nube4.png")
    merry = image.load("goingmerry.png")
    merry = transform.scale(merry, (220, 170))
    xm = 0
    mixer.music.load("soundtrack2.mp3")
    mixer.music.play(-1)
    while True:
       screen.fill((255,255,255))
       for e in event.get():
           if e.type == QUIT: sys.exit()
           if e.type == KEYDOWN and K_d: 
            activo1 = True
       screen.blit(fondo1, (0,0))
       screen.blit(fondo2, (0,100))
       screen.blit(nube1, (50,50))
       screen.blit(nube2, (500, 100))
       screen.blit(nube3, (150, 200))
       screen.blit(nube4, (700, 250))
       screen.blit(merry, (xm, 420))
       #bv1 = pirateFont.render("Bienvenido Pirata!", True, (255,255,255))
       bv2 = pirateFont.render("Avanza para jugar", True, (255,255,255))
       bv3 = pirateFont.render("Presiona 1 para las instrucciones", True, (255,255,255))
       #screen.blit(bv1, (170, 100))
       screen.blit(bv2, (300, 240))
       screen.blit(bv3, (220, 260))
       if key.get_pressed()[K_d]: xm = (xm + 3) 
       if xm > 800: return 2
       display.flip()
       
def cargaranim(prefijo,sufijo,n):
    images = []
    for i in range(1, n+1):
        name = prefijo+str(i)+sufijo
        images.append(image.load(name))
    return images

def mostraranim(images, freq, x, y):
    frame = int(time.time()*freq) % len(images)
    screen.blit(images[frame], (100,100))
    
acem = cargaranim("acem/ace_",".png",8) 
acev = cargaranim("acev/ace_",".png",7)
acee = cargaranim("acee/ace_",".png",5)
mor = cargaranim("morgan/morgan_", ".png", 5)

def Morgan(escena):
    global activo
    print("Morgan Inicia")
    fondomor = image.load("fondomorgan.png")
    fondomor = transform.scale(fondomor, (800,600))
    mixer.music.load("soundtrack1.mp3")
    ace_normal = image.load("aceotrave.png")
    ace_normal = transform.scale(ace_normal, (200, 200))
    mixer.music.play(-1)
    while True:
        screen.fill((255,255,255))
        ex, ye = 0,0
        #for e in event.get():
        #    if e.type == QUIT: sys.exit()
        #    if e.type == KEYDOWN and e.key == K_d:
        #        if e.type == KEYDOWN and e.key == K_d:
        #            if e.type == KEYDOWN and e.key == K_a:
        #                if e.type == KEYDOWN and e.key == K_a: return 3 
        #    if e.type == KEYDOWN and e.key == K_p: return 3
        screen.blit(fondomor, (0,0))
        screen.blit(ace_normal, (ex, ye))
        #load
        ins1 = pirateFont.render("Pirata, ataca!", True, (255,255,255))
        screen.blit(ins1, (300, 10))
        display.flip()
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_d:
                print("Derecha")
                ex+=velocity
def Vista(escena):
    global activo
    fondovis = image.load("fondovista.png")
    fondovis = transform.scale(fondovis, (800,600))
    mixer.music.load("soundtrack1.mp3")
    mixer.music.play(-1)
    while True:
        screen.fill((255,255,255))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_p: return 4
        screen.blit(fondovis, (0,0))
        ins2 = pirateFont.render("No lo dejes escapar!", True, (255,255,255))
        screen.blit(ins2, (250,10))
        display.flip()
        
def Enel(escena):
    global activo
    cielo = image.load("cieloenel.png")
    cielo = transform.scale(cielo,(800,600))
    fondoenel = image.load("fondoenel.png")
    fondoenel = transform.scale(fondoenel, (800,600))
    while True:
        screen.fill((255,255,255))
        for e in event.get():
            if e.type == QUIT: sys.exit()
        screen.blit(cielo, (0,0))
        screen.blit(fondoenel, (0,0))
        ins3 = pirateFont.render("Tan solo queda uno, acabalo!", True, (255,255,255))
        screen.blit(ins3, (250, 10))
        display.flip()
        return escena
    

escena = 1

while True:
   if escena == 1:escena = Inicio(escena)
   elif escena == 2: escena = Morgan(escena)
   elif escena == 3: escena = Vista(escena)
   elif escena == 4: escena = Enel(escena)
   elif activo1 == True: mostraranim(acem)
