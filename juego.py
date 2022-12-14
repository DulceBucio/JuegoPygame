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
    ins = True 
    mixer.music.load("soundtrack2.mp3")
    mixer.music.play(1)
    while True:
       screen.fill((255,255,255))
       for e in event.get():
           if e.type == QUIT: sys.exit()
           if e.type == KEYDOWN and e.key == K_1: ins = False
       screen.blit(fondo1, (0,0))
       screen.blit(fondo2, (0,100))
       screen.blit(nube1, (50,50))
       screen.blit(nube2, (500, 100))
       screen.blit(nube3, (150, 200))
       screen.blit(nube4, (700, 250))
       screen.blit(merry, (xm, 420))
       screen.blit(logo, (100, 0))
       bv1 = pirateFont.render("Avanza con D para jugar", True, (255,255,255))
       bv2 = pirateFont.render("Presiona 1 para las instrucciones", True, (255,255,255))
       bv3 = pirateFont.render("Te enfrentaras a los villanos mas feroces de todo el mar, pero cuidado", True, (255,255,255))
       bv4 = pirateFont.render("solo puedes derrotarlos cuidadosamente con cierto patron de ataques", True, (255,255,255))
       if ins:
        screen.blit(bv1, (260, 250))
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
    screen.blit(images[frame], (x,y))
    
acem = cargaranim("acem/ace_",".png",8) 
acev = cargaranim("acev/ace_",".png",7)
acee = cargaranim("acee/ace_",".png",5)
mor = cargaranim("morgan/morgan_", ".png", 5)
vis = cargaranim("vista/vista_", ".png", 5)
enel = cargaranim("enel/enel_", ".png", 3)

def Morgan(escena):
    fondomor = image.load("fondomorgan.png")
    fondomor = transform.scale(fondomor, (800,600))
    ace_normal = image.load("acetieso1.png")
    ace_normal = transform.scale(ace_normal, (200, 200))
    mostrara1 = False
    mostraracet = True
    teclas = ""
    num = random.randint(1,2)
    solucion = ("d"*num + "a"*num) * 3
    x1 = 200
    pasa = False
    mixer.music.load("soundtrack1.mp3")
    mixer.music.play(1)
    golpe = mixer.Sound("golpe.mp3")
    mostrarv = True 
    while True:
        screen.fill((255,255,255))
        for e in event.get():
            if e.type == KEYDOWN and e.key == K_p and pasa: return 3
            if e.type == KEYDOWN and e.key == K_o: return 2
            if e.type == KEYDOWN and e.key == K_d: 
                teclas = teclas + chr(e.key)
                mostrara1 = True
                mostraracet = False
                x1 = x1 + 20
                golpe.play()
            if e.type == KEYDOWN and e.key == K_a: 
                teclas = teclas + chr(e.key)
                x1 = x1 + 20
                golpe.play()
        screen.blit(fondomor, (0,0))
        if mostraracet: screen.blit(ace_normal, (x1,250)) 
        if mostrara1:
            mostraranim(acem, 10, x1, 250)
        if len(teclas) >= len(solucion):
            if teclas == solucion:
                ins4 = pirateFont.render("Felicidades pirata, continua con P!", True, (255,255,255))
                screen.blit(ins4, (200, 500))
                pasa = True 
                mostrarv = False
                mostraracet = True 
                mostrara1 = False
            else: 
                ins5 = pirateFont.render("Morgan sigue muy fuerte! Vuelve a intentarlo con O", True, (255,255,255))
                screen.blit(ins5, (100, 500))
        if mostrarv: mostraranim(mor, 10, 500, 250)
        ins1 = pirateFont.render(solucion, True, (255,255,255))
        ins2 = pirateFont.render("Usa las teclas: ", True, (255,255,255))
        ins3 = pirateFont.render("para derrotar a Morgan!", True, (255,255,255))
        screen.blit(ins1, (300, 40))
        screen.blit(ins2, (300,10))
        screen.blit(ins3, (250, 70))
        display.flip()

def Vista(escena):
    fondovis = image.load("fondovista.png")
    fondovis = transform.scale(fondovis, (800,600))
    ace_normal = image.load("acetieso1.png")
    ace_normal = transform.scale(ace_normal, (200, 200))
    mostraracet = True
    teclas = ""
    num = random.randint(1,2)
    solucion = ("d"*num + "a"*num + "w"*num) * 4
    mostraracet = True
    mostrara1 = False 
    pasa = False
    mixer.music.load("soundtrack1.mp3")
    mixer.music.play(1)
    golpe = mixer.Sound("golpe.mp3")
    mostrarv = True
    x1 = 200
    while True:
        screen.fill((255,255,255))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_p and pasa: return 4
            if e.type == KEYDOWN and e.key == K_o: return 3
            if e.type == KEYDOWN and e.key == K_d: 
                teclas = teclas + chr(e.key)
                mostrara1 = True
                mostraracet = False
                x1 = x1 + 10
                golpe.play()
            if e.type == KEYDOWN and e.key == K_a: 
                teclas = teclas + chr(e.key)
                x1 = x1 + 10
                golpe.play()
            if e.type == KEYDOWN and e.key == K_w: 
                teclas = teclas + chr(e.key)
                x1 = x1 + 10
                golpe.play()
        screen.blit(fondovis, (0,0))
        if mostrara1:
            mostraranim(acev, 10, x1, 250)
        if mostraracet: screen.blit(ace_normal, (x1,250))
        if mostrarv: mostraranim(vis, 10, 500, 250)
        ins1 = pirateFont.render(solucion, True, (255,255,255))
        ins2 = pirateFont.render("Usa las teclas: ", True, (255,255,255))
        ins3 = pirateFont.render("para derrotar a Vista!", True, (255,255,255))
        if len(teclas) >= len(solucion):
            if teclas == solucion:
                ins4 = pirateFont.render("Felicidades pirata, continua con P!", True, (255,255,255))
                screen.blit(ins4, (200, 490))
                pasa = True
                mostrarv = False
                mostraracet = True 
                mostrara1 = False
            else: 
                ins5 = pirateFont.render("Vista sigue muy fuerte! Vuelve a intentarlo con O", True, (255,255,255))
                screen.blit(ins5, (100, 490))
        screen.blit(ins1, (200, 540))
        screen.blit(ins2, (300,510))
        screen.blit(ins3, (250, 570))
        display.flip()
        
def Enel(escena):
    cielo = image.load("cieloenel.png")
    cielo = transform.scale(cielo,(800,600))
    fondoenel = image.load("fondoenel.png")
    fondoenel = transform.scale(fondoenel, (800,600))
    ace_normal = image.load("acetieso1.png")
    ace_normal = transform.scale(ace_normal, (200, 200))
    teclas = ""
    num = random.randint(1,2)
    solucion = ("d"*num + "a"*num + "w"*num + "s"*num) * 5
    mostraracet = True
    mostrara1 = False
    pasa = False
    mixer.music.load("soundtrack1.mp3")
    mixer.music.play(1)
    golpe = mixer.Sound("golpe.mp3")
    mostrarv = True 
    x1 = 200
    while True:
        screen.fill((255,255,255))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_p and pasa: return 5
            if e.type == KEYDOWN and e.key == K_o: return 4
            if e.type == KEYDOWN and e.key == K_d: 
                teclas = teclas + chr(e.key)
                mostrara1 = True
                mostraracet = False
                golpe.play()
                x1 = x1 + 5
            if e.type == KEYDOWN and e.key == K_a: 
                teclas = teclas + chr(e.key)
                golpe.play()
                x1 = x1 + 5
            if e.type == KEYDOWN and e.key == K_w: 
                teclas = teclas + chr(e.key)
                golpe.play()
                x1 = x1 + 5
            if e.type == KEYDOWN and e.key == K_s: 
                teclas = teclas + chr(e.key)
                golpe.play()
                x1 = x1 + 5
        screen.blit(fondoenel, (0,0))
        if mostraracet: screen.blit(ace_normal, (x1,250))
        if mostrara1:
            mostraranim(acee, 10, x1, 250)
        if mostrarv: mostraranim(enel, 3, 500, 250)
        ins1 = pirateFont.render(solucion, True, (255,255,255))
        ins2 = pirateFont.render("Usa las teclas: ", True, (255,255,255))
        ins3 = pirateFont.render("para derrotar a Enel", True, (255,255,255))
        screen.blit(ins1, (200, 540))
        screen.blit(ins2, (300,510))
        screen.blit(ins3, (250, 570))
        if len(teclas) >= len(solucion):
            if teclas == solucion:
                ins4 = pirateFont.render("Felicidades pirata, recoge tu botin con P", True, (255,255,255))
                screen.blit(ins4, (200, 490))
                pasa = True
                mostrarv = False
                mostraracet = True 
                mostrara1 = False
            else: 
                ins5 = pirateFont.render("Enel sigue muy fuerte! Vuelve a intentarlo con O", True, (255,255,255))
                screen.blit(ins5, (100, 490))
        display.flip()

def final(escena):
    fondof = image.load("escenafinal.jpg")
    fondof = transform.scale(fondof, (800,600))
    mixer.music.load("soundtrackf.mp3")
    mixer.music.play(1)
    while True:
        screen.fill((255,255,255))
        for e in event.get():
            if e.type == QUIT: sys.exit()
        screen.blit(fondof, (0,0))
        text = pirateFont.render("Enhorabuena pirata!", True, (255,255,255))
        screen.blit(text, (300, 560))
        display.flip()
    

    

escena = 1

while True:
   if escena == 1:escena = Inicio(escena)
   elif escena == 2: escena = Morgan(escena)
   elif escena == 3: escena = Vista(escena)
   elif escena == 4: escena = Enel(escena)
   elif escena == 5: escena = final(escena) 
