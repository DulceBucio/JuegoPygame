from pygame import *
import sys, time
import random

init() 
screen = display.set_mode((800,600)) 
pirateFont = font.Font("Pirate Ship.ttf", 20)

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
    logo = image.load("logojuego.png")
    logo = transform.scale(logo, (600, 250))
    #mixer.music.load("soundtrack2.mp3")
    #mixer.music.play(-1)
    ins = True 
    while True:
       screen.fill((255,255,255))
       for e in event.get():
           if e.type == QUIT: sys.exit()
           if e.type == KEYDOWN and K_a: ins = False
       screen.blit(fondo1, (0,0))
       screen.blit(fondo2, (0,100))
       screen.blit(nube1, (50,50))
       screen.blit(nube2, (500, 100))
       screen.blit(nube3, (150, 200))
       screen.blit(nube4, (700, 250))
       screen.blit(merry, (xm, 420))
       screen.blit(logo, (100, 0))
       bv1 = pirateFont.render("Avanza para jugar", True, (255,255,255))
       bv2 = pirateFont.render("Presiona 1 para las instrucciones", True, (255,255,255))
       bv3 = pirateFont.render("Te enfrentaras a los villanos mas feroces de todo el mar, pero cuidado", True, (255,255,255))
       bv4 = pirateFont.render("solo puedes derrotarlos cuidadosamente con cierto patron de ataques", True, (255,255,255))
       if ins:
        screen.blit(bv1, (300, 250))
        screen.blit(bv2, (220, 270))
       else: 
        screen.blit(bv3, (0,250))
        screen.blit(bv4, (0,280))
       if key.get_pressed()[K_d]: xm = (xm + 3) 
       if xm > 800: return 2
       display.flip()
       
def cargaranim(prefijo,sufijo,n):
    images = []
    for i in range(1, n+1):
        name = prefijo+str(i)+sufijo
        anim = transform.scale(image.load(name), (200,200))
        images.append(anim)
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
    fondomor = image.load("fondomorgan.png")
    fondomor = transform.scale(fondomor, (800,600))
    #mixer.music.load("soundtrack1.mp3")
    ace_normal = image.load("acetieso1.png")
    ace_normal = transform.scale(ace_normal, (200, 200))
    #mixer.music.play(-1)
    mostrara1 = False
    teclas = ""
    num = random.randint(1,2)
    solucion = ("d"*num + "a"*num) * 3
    while True:
        screen.fill((255,255,255))
        for e in event.get():
            if e.type == KEYDOWN and e.key == K_p: return 3
            if e.type == KEYDOWN: 
                mostrara1 = True
                teclas = teclas + chr(e.key)
                print(teclas)
        screen.blit(fondomor, (0,0))
        screen.blit(ace_normal, (200,250))
        if mostrara1:
            mostraranim(acem, 10, 300, 350)
        if teclas == solucion: print("si")
        #load
        ins1 = pirateFont.render(solucion, True, (255,255,255))
        screen.blit(ins1, (300, 10))
        display.flip()
def Vista(escena):
    global activo
    fondovis = image.load("fondovista.png")
    fondovis = transform.scale(fondovis, (800,600))
    #mixer.music.load("soundtrack1.mp3")
    #mixer.music.play(-1)
    teclas = ""
    num = random.randint(1,2)
    solucion = ("d"*num + "a"*num + "w"*num) * 4
    while True:
        screen.fill((255,255,255))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_p: return 4
        if teclas == solucion: print("si")
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
    teclas = ""
    num = random.randint(1,2)
    solucion = ("d"*num + "a"*num + "w"*num + "s") * 5
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

