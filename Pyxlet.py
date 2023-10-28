import pygame
import pygame.font
import sys
import os
import math
import random
import numpy
import tkinter
import matplotlib.image
from tkinter import filedialog
from random import randint
from PIL import Image, ImageOps
from matplotlib import pyplot as plt
from pygame.locals import *


#path
imgpath = "data/images/"
fontpath = "data/fonts/"

#settings
w = 1280
h = 720
scale = w / 1920
imgw = 18
imgh = 18
imgw2 = 20
imgh2 = 20
midx = 1085 * scale

#images
icon = pygame.image.load(imgpath + 'icon.png')
background = pygame.image.load(imgpath + 'background3.png')
background = pygame.transform.scale(background, (w, h))
drawicon = pygame.image.load(imgpath + 'draw.png')
drawicon = pygame.transform.scale(drawicon, (int(50 * scale), int(50 * scale)))
eraseicon = pygame.image.load(imgpath + 'erase.png')
eraseicon = pygame.transform.scale(eraseicon, (int(50 * scale), int(50 * scale)))
fillicon = pygame.image.load(imgpath + 'fill.png')
fillicon = pygame.transform.scale(fillicon, (int(50 * scale), int(50 * scale)))
gridicon = pygame.image.load(imgpath + 'gon.png')
gridicon = pygame.transform.scale(gridicon, (int(50 * scale), int(50 * scale)))
bgfillicon = pygame.image.load(imgpath + 'bgfill.png')
bgfillicon = pygame.transform.scale(bgfillicon, (int(50 * scale), int(50 * scale)))
fscreenicon = pygame.image.load(imgpath + 'fscreen.png')
fscreenicon = pygame.transform.scale(fscreenicon, (int(50 * scale), int(50 * scale)))
creadericon = pygame.image.load(imgpath + 'creader.png')
creadericon = pygame.transform.scale(creadericon, (int(50 * scale), int(50 * scale)))
helpicon = pygame.image.load(imgpath + 'help.png')
helpicon = pygame.transform.scale(helpicon, (int(50 * scale), int(50 * scale)))
centericon = pygame.image.load(imgpath + 'center.png')
centericon = pygame.transform.scale(centericon, (int(50 * scale), int(50 * scale)))
rgb = pygame.image.load(imgpath + 'rgb.png')
rgb = pygame.transform.scale(rgb, (251 * scale, 251 * scale))
helpbox = pygame.image.load(imgpath + 'helpbox.png')
helpbox = pygame.transform.scale(helpbox, (300 * scale, 540 * scale))

#preettings
pygame.init()
flags = DOUBLEBUF | FULLSCREEN | HWSURFACE
screen = pygame.display.set_mode((w, h))
pygame.display.set_icon(icon)
pygame.display.set_caption("Pyxlet")
pygame.key.set_repeat(1, 30)
clock = pygame.time.Clock()


#variables
imgname = ['p', 'i', 'c', 't', 'u', 'r', 'e']
grid1 = ['2', '0']
grid2 =['2', '0']
rlist = ['0']
glist = ['0']
blist = ['0']
fpslist = ['1', '0']
color = (0, 0, 0)
bgcolor = (255, 255, 255)
alpha = 1
tool = 1
layers = 1
selectedlayer = 1
animationcounter = 0
animationtimer = 10
layershift = 0
layervis1 = True
zoom = 1
mx2, my2 = pygame.mouse.get_pos()
xshift = 0
yshift = 0
xshift2 = 0
yshift2 = 0
grid = 'on'
namestatus = False
animationstatus = False
gridstatus = False
rstatus = False
gstatus = False
bstatus = False
fpsstatus = False
helpstatus = False
shiftstatus = False
mousefunc = False
fillfunc = True
screensize = False
imgarr1 = numpy.array([[[1.0, 1.0, 1.0 ,0.0] for y in range(imgh)] for z in range(imgw)])
imgarr = numpy.array([[[1.0, 1.0, 1.0 ,0.0] for y in range(imgh)] for z in range(imgw)])
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#FONTS
font = pygame.font.Font(fontpath + 'font.ttf', 12)
font2 = pygame.font.Font(fontpath + 'font.ttf', 20)
font3 = pygame.font.Font(fontpath + 'font.ttf', 10)
pyxlettext = font2.render('PYXLET', 1, (0, 0, 0))
newtext = font.render('NEW', 1, (0, 0, 0))
savetext = font.render('SAVE', 1, (0, 0, 0))
opentext = font.render('OPEN', 1, (0, 0, 0))
nametext = font.render('NAME:', 1, (0, 0, 0))
rtext = font.render('R:' + str(color[0]), 1, (0, 0, 0))
gtext = font.render('G:' + str(color[1]), 1, (0, 0, 0))
btext = font.render('B:' + str(color[2]), 1, (0, 0, 0))
plustext = font2.render('+' , 1, (0, 0, 0))
minustext = font2.render('-' , 1, (0, 0, 0))
alphatext = font.render('α:' + str(alpha), 1, (0, 0, 0))
gridtext = font.render(str(imgw2) + ' x ' + str(imgh2), 1, (0, 0, 0))
layerstext = font3.render('LAYERS', 1, (0, 0, 0))
settingstext = font3.render('SETTINGS', 1, (0, 0, 0))
toolstext = font3.render('TOOLS', 1, (0, 0, 0))
fpsanimationtext = font3.render('fps: ' + str(animationtimer), 1, (0, 0, 0))

#functions
def drawcanvas(x, y):
    global cw
    global ch
    global alpha
    global imgarr
    ch = int(690 / y) * y
    cw = int(690 / y) * x
    imgarr = numpy.array([[[1.0, 1.0, 1.0 ,0.0] for y in range(imgh)] for z in range(imgw)])
    for i in range(layers):
        for j in range(x):
            for k in range(y):
                p = i + 1
                if globals()['layervis%s' % p] == True:
                    arr = globals()['imgarr%s' % p]
                    if arr[j][k][3] != float(0):
                        imgarr[j][k][0] = arr[j][k][0]
                        imgarr[j][k][1] = arr[j][k][1]
                        imgarr[j][k][2] = arr[j][k][2]
                        imgarr[j][k][3] = arr[j][k][3]
                        
    if animationstatus == False:            
        for i in range(x):
            for j in range(y):
                if imgarr[i][j][3] != 0:
                    pygame.draw.rect(screen, (int(255 * imgarr[i][j][0]), int(255 * imgarr[i][j][1]), int(255 * imgarr[i][j][2])), (((((1085 - cw / 2) + int(690 / y) * i) * scale) + xshift) * zoom, (((120 + int(690 / y) * j) * scale) + yshift) * zoom, (int(690 / y) + 1) * scale * zoom, (int(690 / y) + 1) * scale * zoom), 0)
            pygame.draw.rect(screen, (0, 0, 0), ((((1085 - cw / 2) * scale) + xshift) * zoom, ((120 * scale) + yshift) * zoom, cw * scale * zoom, ch * scale * zoom), 1)
    else:
        for i in range(x):
            for j in range(y):
                if globals()['imgarr%s' % selectedlayer][i][j][3] != 0:
                    pygame.draw.rect(screen, (int(255 * globals()['imgarr%s' % selectedlayer][i][j][0]), int(255 * globals()['imgarr%s' % selectedlayer][i][j][1]), int(255 * globals()['imgarr%s' % selectedlayer][i][j][2])), (((((1085 - cw / 2) + int(690 / y) * i) * scale) + xshift), (((120 + int(690 / y) * j) * scale) + yshift), (int(690 / y) + 1) * scale, (int(690 / y) + 1) * scale), 0)
            pygame.draw.rect(screen, (0, 0, 0), ((((1085 - cw / 2) * scale) + xshift) * zoom, ((120 * scale) + yshift) * zoom, cw * scale * zoom, ch * scale * zoom), 1)

    if grid == 'on':
        for i in range(x):
            i += 1
            pygame.draw.line(screen, (0, 0, 0), ((((1085 - cw / 2 + i * int(690 / y)) * scale) + xshift) * zoom, ((120 * scale) + yshift) * zoom), ((((1085 - cw / 2 + i * int(690 / y)) * scale) + xshift) * zoom, (((120 + ch) * scale) + yshift) * zoom), 1)
        for i in range(y):
            i += 1
            pygame.draw.line(screen, (0, 0, 0), ((((1085 - cw / 2) * scale) + xshift) * zoom, (((120 + i * int(690 / y)) * scale) + yshift) * zoom), ((((1085 + cw / 2) * scale) + xshift) * zoom, (((120 + i * int(690 / y)) * scale) + yshift) * zoom), 1)

def drawcanvas2(x, y):
    global cw
    global ch
    global alpha
    global imgarr
    cc = min((100/y), (180/x))
    ch2 = int(cc * y)
    cw2 = int(cc * x)
    for k in range(layers):
        if k + 1 - layershift > 0 and k + 1 - layershift <= 6:
            for i in range(x):
                    for j in range(y):
                        p = k + 1
                        if globals()['imgarr%s' % p][i][j][3] != 0:
                            pygame.draw.rect(screen, (int(255 * globals()['imgarr%s' % p][i][j][0]), int(255 * globals()['imgarr%s' % p][i][j][1]), int(255 * globals()['imgarr%s' % p][i][j][2])), ((((410 + (220  * (k - layershift))) + (200 - cw2) / 2) + int(cc * i)) * scale, (910 + ((120 - ch2) / 2) + int(cc * (j))) * scale, int((cc + 2) * scale), int((cc + 2) * scale)), 0)
                        #pygame.draw.rect(screen, (0, 0, 0), (((410 + (220 * (k - layershift) + (200 - cw2) / 2))) * scale, (910 + ((120 - ch2) / 2)) * scale, cw2 * scale, ch2 * scale), 1)

def getpixelpos(x, y):
    global ch
    global cw
    global imgw
    global imgh
    global scale
    global color
    global tool
    global alpha
    global fillfunc
    global xshift
    global yshift
    x1 = ((x - xshift) - (1085 - cw / 2) * scale) // (int(690 / imgh) * scale) * zoom
    y1 = ((y - yshift) - 120 * scale) // (int(690 / imgh) * scale) * zoom
    if tool == 1:
        globals()['imgarr%s' % selectedlayer][int(x1)][int(y1)] = [float(color[0]/255), float(color[1]/255), float(color[2]/255), float(alpha)]
    elif tool == 2:
        globals()['imgarr%s' % selectedlayer][int(x1)][int(y1)] = [float(1), float(1), float(1), float(0)]
    elif tool == 3 and fillfunc == True:
        fillfunc = False
        pixeltofill = [[x1, y1]]
        c1 = globals()['imgarr%s' % selectedlayer][int(x1)][int(y1)][0]
        c2 = globals()['imgarr%s' % selectedlayer][int(x1)][int(y1)][1]
        c3 = globals()['imgarr%s' % selectedlayer][int(x1)][int(y1)][2]
        color2 = (c1, c2, c3)
        if color2 != color:
            while len(pixeltofill) > 0:
                xx = int(pixeltofill[0][0])
                yy = int(pixeltofill[0][1])
                pixeltofill.pop(0)
                if (xx + 1) < imgw:
                    if float(color2[0]) == globals()['imgarr%s' % selectedlayer][xx + 1][yy][0] and float(color2[1]) == globals()['imgarr%s' % selectedlayer][xx + 1][yy][1] and float(color2[2]) == globals()['imgarr%s' % selectedlayer][xx + 1][yy][2]:
                        pixeltofill.append([xx + 1, yy])
                        globals()['imgarr%s' % selectedlayer][xx + 1][yy] = [float(color[0]/255), float(color[1]/255), float(color[2]/255), float(alpha)]
                if (xx - 1) >= 0:     
                    if float(color2[0]) == globals()['imgarr%s' % selectedlayer][xx - 1][yy][0] and float(color2[1]) == globals()['imgarr%s' % selectedlayer][xx - 1][yy][1] and float(color2[2]) == globals()['imgarr%s' % selectedlayer][xx - 1][yy][2]:
                        pixeltofill.append([xx - 1, yy])
                        globals()['imgarr%s' % selectedlayer][xx - 1][yy] = [float(color[0]/255), float(color[1]/255), float(color[2]/255), float(alpha)]
                if (yy + 1) < imgh:
                    if float(color2[0]) == globals()['imgarr%s' % selectedlayer][xx][yy + 1][0] and float(color2[1]) == globals()['imgarr%s' % selectedlayer][xx][yy + 1][1] and float(color2[2]) == globals()['imgarr%s' % selectedlayer][xx][yy + 1][2]:
                        pixeltofill.append([xx, yy + 1])
                        globals()['imgarr%s' % selectedlayer][xx][yy + 1] = [float(color[0]/255), float(color[1]/255), float(color[2]/255), float(alpha)]
                if (yy - 1) >= 0:
                    if float(color2[0]) == globals()['imgarr%s' % selectedlayer][xx][yy - 1][0] and float(color2[1]) == globals()['imgarr%s' % selectedlayer][xx][yy - 1][1] and float(color2[2]) == globals()['imgarr%s' % selectedlayer][xx][yy - 1][2]:
                        pixeltofill.append([xx, yy - 1])
                        globals()['imgarr%s' % selectedlayer][xx][yy - 1] = [float(color[0]/255), float(color[1]/255), float(color[2]/255), float(alpha)]
                globals()['imgarr%s' % selectedlayer][xx][yy] = [float(color[0]/255), float(color[1]/255), float(color[2]/255), float(alpha)]                     
    elif tool == 4:
        color = screen.get_at(pygame.mouse.get_pos())[:3]
        tool = 1

            
    

main = True
while main:
    clock.tick(60)
    screen.fill(bgcolor)
    mx, my = pygame.mouse.get_pos()
    if shiftstatus == True:
        xshift = xshift2 + mx - mx2
        yshift = yshift2 + my - my2
    rtext = font.render('R:' + str(color[0]), 1, (0, 0, 0))
    gtext = font.render('G:' + str(color[1]), 1, (0, 0, 0))
    btext = font.render('B:' + str(color[2]), 1, (0, 0, 0))
    fpsanimationtext = font.render('fps: ' + str(animationtimer), 1, (0, 0, 0))
    drawcanvas(imgw, imgh)
    screen.blit(background, (0, 0))
    screen.blit(fpsanimationtext, (1768 * scale, 997 * scale))
    screen.blit(pyxlettext, (25, 12))
    screen.blit(drawicon, (30 * scale, 70 * scale))
    screen.blit(eraseicon, (130 * scale, 70 * scale))
    screen.blit(fillicon, (230 * scale, 70 * scale))
    screen.blit(creadericon, (30 * scale, 160 * scale))
    screen.blit(bgfillicon, (130 * scale, 160 * scale))
    screen.blit(centericon, (230 * scale, 160 * scale))
    screen.blit(gridicon, (30 * scale, 520 * scale))
    screen.blit(fscreenicon, (130 * scale, 520 * scale))
    screen.blit(helpicon, (230 * scale, 520 * scale))
    screen.blit(rgb, (30 * scale, 710 * scale))
    screen.blit(rtext, (90 * scale, 1010 * scale))
    screen.blit(gtext, (145 * scale, 1010 * scale))
    screen.blit(btext, (200 * scale, 1010 * scale))
    screen.blit(alphatext, (255 * scale, 1010 * scale))
    screen.blit(gridtext, (235 * scale, 25 * scale))
    screen.blit(newtext, (335 * scale, 25 * scale))
    screen.blit(savetext, (465 * scale, 25 * scale))
    screen.blit(opentext, (595 * scale, 25 * scale))
    screen.blit(nametext, (725 * scale, 25 * scale))
    screen.blit(plustext, (355 * scale, 925 * scale))
    screen.blit(minustext, (360 * scale, 990 * scale))
    screen.blit(toolstext, (40 * scale, 411 * scale))
    screen.blit(settingstext, (40 * scale, 682 * scale))
    screen.blit(layerstext, (360 * scale, 1047 * scale))
    nametext2 = font.render(str(''.join(imgname)), 1, (0, 0, 0))
    screen.blit(nametext2, (780 * scale, 25 * scale))
    
    if main:
        pygame.draw.rect(screen, color, (30 * scale, 990 * scale, 50 * scale, 50 * scale))
        pygame.draw.rect(screen, (255, 255, 255), (30 * scale, 990 * scale, 50 * scale, 50 * scale), 2)

    if tool == 1:
        pygame.draw.rect(screen, (255, 0, 0), (30 * scale, 70 * scale, 50 * scale, 50 * scale), 1)

    elif tool == 2:
        pygame.draw.rect(screen, (255, 0, 0), (130 * scale, 70 * scale, 50 * scale, 50 * scale), 1)

    elif tool == 3:
        pygame.draw.rect(screen, (255, 0, 0), (230 * scale, 70 * scale, 50 * scale, 50 * scale), 1)

    elif tool == 4:
        pygame.draw.rect(screen, (255, 0, 0), (30 * scale, 160 * scale, 50 * scale, 50 * scale), 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();sys.exit
            main = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                pygame.quit();sys.exit
                main = False
                
        elif event.type == pygame.KEYUP:
            #print(pygame.key.name(event.key))
            if event.key == ord(' '):
                animationstatus = not animationstatus
            if namestatus == True:
                if event.key == 8 and len(imgname) > 0:
                    del imgname[len(imgname) - 1]
                elif event.key >= 97 and event.key <= 123:
                    imgname.append(letters[event.key - 97])
                elif event.key >= 48 and event.key <= 57:
                    imgname.append(str(event.key - 48))
                elif event.key == 13:
                    namestatus = not namestatus
            elif gridstatus == True:
                if event.key == 8:
                    if gridpos == 1 and len(grid1) > 0:
                        del grid1[len(grid1) - 1]
                    elif gridpos == 2 and len(grid2) > 0:
                        del grid2[len(grid2) - 1]
                elif event.key >= 48 and event.key <= 57:
                    if gridpos == 1:
                        grid1.append(str(event.key - 48))
                    else:
                        grid2.append(str(event.key - 48))
                elif event.key == 13:
                    if gridpos == 1:
                        gridpos = 2
                    else:
                        gridstatus = not gridstatus
                if len(grid1) > 0:
                    imgw2 = int(str(''.join(grid1)))
                else:
                    imgw2 = 0
                if len(grid2) > 0:
                    imgh2 = int(str(''.join(grid2)))
                else:
                    imgh2 = 0
                if imgw2 > 50:
                    imgw2 = 50
                    grid1 = ['1', '0', '0']
                if imgh2 > 50:
                    imgh2 = 50
                    grid2 = ['1', '0', '0']
                gridtext = font.render(str(imgw2) + ' x ' + str(imgh2), 1, (0, 0, 0))
            elif rstatus == True:
                if event.key == 8 and len(rlist) > 0:
                    if len(rlist) == 1:
                        rlist = ['0']
                    else:
                        del rlist[len(rlist) - 1]
                elif event.key >= 48 and event.key <= 57:
                    rlist.append(str(event.key - 48))
                elif event.key == 13:
                    rstatus = not rstatus
                if len(rlist) > 0 and int(''.join(rlist)) > 255:
                    rlist = ['2', '5', '5']
                color = (int(''.join(rlist)), color[1], color[2])
            elif gstatus == True:
                if event.key == 8 and len(glist) > 0:
                    if len(glist) == 1:
                        glist = ['0']
                    else:
                        del glist[len(glist) - 1]
                elif event.key >= 48 and event.key <= 57:
                    glist.append(str(event.key - 48))
                elif event.key == 13:
                    gstatus = not gstatus
                if len(glist) > 0 and int(''.join(glist)) > 255:
                    glist = ['2', '5', '5']
                color = (color[0], int(''.join(glist)), color[2])
            elif bstatus == True:
                if event.key == 8 and len(blist) > 0:
                    if len(blist) == 1:
                        blist = ['0']
                    else:
                        del blist[len(blist) - 1]
                elif event.key >= 48 and event.key <= 57:
                    blist.append(str(event.key - 48))
                elif event.key == 13:
                    bstatus = not bstatus
                if len(blist) > 0 and int(''.join(blist)) > 255:
                    blist = ['2', '5', '5']
                color = (color[0], color[1], int(''.join(blist)))
            elif fpsstatus == True:
                if event.key == 8 and len(fpslist) > 0:
                    if len(fpslist) == 1:
                        fpslist = ['0']
                    else:
                        del fpslist[len(fpslist) - 1]
                elif event.key >= 48 and event.key <= 57:
                    fpslist.append(str(event.key - 48))
                elif event.key == 13:
                    fpsstatus = not fpsstatus
                if len(fpslist) > 0 and int(''.join(fpslist)) > 30:
                    fpslist = ['3', '0']
                animationtimer = (int(''.join(fpslist)))
                    
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            namestatus = False
            animationstatus = False
            gridstatus = False
            rstatus = False
            gstatus = False
            bstatus = False
            fpsstatus = False
            helpstatus = False
            #der selectedlayer unten im feld gerückt werden dass er angezeigt wird wenn man irgendwo hinklickt.
            #if selectedlayer - layershift <= 0:
             #   layershift = selectedlayer - 1
            #if selectedlayer > layershift + 6:
             #   layershift = selectedlayer - 6
            
            if event.button == 1:
                if mx > ((1085 - cw / 2) * scale) + xshift and mx < ((1085 + cw / 2) * scale) + xshift and my > (120 * scale) + yshift and my < ((120 + ch) * scale) + yshift or mx > 30 * scale and mx < 280 * scale and my > 710 * scale and my < 960 * scale:
                    mousefunc = True
                #gridsize     
                elif mx > 230 * scale and mx < 280 * scale and my > 20 * scale and my < 40 * scale:
                    gridstatus = True
                    gridpos = 1
                elif mx > 280 * scale and mx < 330 * scale and my > 20 * scale and my < 40 * scale:
                    gridstatus = True
                    gridpos = 2
                #new
                elif mx > 330 * scale and mx < 420 * scale and my > 20 * scale and my < 40 * scale:
                    pygame.draw.rect(screen, (255, 0, 0), (330 * scale, 20 * scale, 90 * scale, 20 * scale), 1)
                    pygame.display.flip()
                    pygame.time.wait(300)
                    imgw = imgw2
                    imgh = imgh2
                    if imgw > 0 and imgh > 0:
                        imgarr1 = numpy.array([[[1.0, 1.0, 1.0 ,0.0] for y in range(imgh)] for z in range(imgw)])
                        imgarr = numpy.array([[[1.0, 1.0, 1.0 ,0.0] for y in range(imgh)] for z in range(imgw)])
                        globals()['layervis%s' % layers] = True
                    layers = 1
                    selectedlayer = 1
                    layershift = 0
                    xshift = 0
                    yshift = 0
                    xshift2 = 0
                    yshift2 = 0
                    zoom = 1
                #save
                elif mx > 460 * scale and mx < 550 * scale and my > 20 * scale and my < 40 * scale:
                    savepath = filedialog.askdirectory()
                    try:
                        picturecount += 1
                    except:
                        picturecount = 1
                    try:
                        matplotlib.image.imsave(savepath + '/' + ''.join(imgname) + '.png', imgarr)
                        originalimg = Image.open(savepath + '/' + ''.join(imgname) + '.png')
                        rotatedimg = originalimg.transpose(Image.ROTATE_270)
                        rotatedimg = ImageOps.mirror(rotatedimg)
                        rotatedimg = rotatedimg.save(savepath + '/' + ''.join(imgname) + '.png')
                        pygame.draw.rect(screen, (255, 0, 0), (460 * scale, 20 * scale, 90 * scale, 20 * scale), 1)
                        pygame.display.flip()
                        if picturecount == 1:
                            imgname.append(str(picturecount))
                        else:
                            imgname[int(len(imgname) - 1)] = str(picturecount)
                    except:
                        None
                #open
                elif mx > 590 * scale and mx < 680 * scale and my > 20 * scale and my < 40 * scale:
                    pygame.draw.rect(screen, (255, 0, 0), (590 * scale, 20 * scale, 90 * scale, 20 * scale), 1)
                    pygame.display.flip()
                    pygame.time.wait(300)
                    try:
                        openimg = filedialog.askopenfilename()
                        originalimg2 = Image.open(openimg)
                        rotatedimg2 = originalimg2.transpose(Image.ROTATE_90)
                        rotatedimg2 = ImageOps.flip(rotatedimg2)
                        rotatedimg2 = rotatedimg2.save('delete_.png')
                        imgarr1 = plt.imread('delete_.png')
                        os.remove('delete_.png')
                        imgw = len(imgarr1)
                        imgh = len(imgarr1[0])
                        imgarr = numpy.array([[[1.0, 1.0, 1.0 ,0.0] for y in range(imgh)] for z in range(imgw)])
                        layers = 1
                        selectedlayer = 1
                        xshift = 0
                        yshift = 0
                        xshift2 = 0
                        yshift2 = 0
                        zoom = 1
                    except:
                        None
                #name
                elif mx > 720 * scale and mx < 1110 * scale and my > 20 * scale and my < 40 * scale and gridstatus == False and rstatus == False and gstatus == False and bstatus == False:###
                    namestatus = True
                elif mx > 30 * scale and mx < 80 * scale and my > 70 * scale and my < 120 * scale:
                    tool = 1
                elif mx > 130 * scale and mx < 180 * scale and my > 70 * scale and my < 120 * scale:
                    tool = 2
                elif mx > 230 * scale and mx < 280 *scale and my > 70 * scale and my < 120 * scale:
                    tool = 3
                elif mx > 30 * scale and mx < 80 * scale and my > 160 * scale and my < 210 * scale:
                    tool = 4
                elif mx > 130 * scale and mx < 180 * scale and my > 160 * scale and my < 210 * scale:
                    bgcolor = color
                elif mx > 230 * scale and mx < 280 * scale and my > 160 * scale and my < 210 * scale:
                    xshift = 0
                    yshift = 0
                    xshift2 = 0
                    yshift2 = 0
                    zoom = 1
                elif mx > 30 * scale and mx < 80 * scale and my > 520 * scale and my < 580 * scale:
                    if grid == 'on':
                        grid = 'off'
                        gridicon = pygame.image.load(imgpath + 'goff.png')
                        gridicon = pygame.transform.scale(gridicon, (int(50 * scale), int(50 * scale)))
                    else:
                        grid = 'on'
                        gridicon = pygame.image.load(imgpath + 'gon.png')
                        gridicon = pygame.transform.scale(gridicon, (int(50 * scale), int(50 * scale)))
                elif mx > 130 * scale and mx < 180 * scale and my > 520 * scale and my < 580 * scale:
                    screensize = not screensize
                    if screensize:
                        screen = pygame.display.set_mode((w, h), flags, 32)
                    else:
                        screen = pygame.display.set_mode((w, h))
                elif mx > 230 * scale and mx < 280 * scale and my > 520 * scale and my < 580 * scale:
                    helpstatus = True
                elif mx > 87 * scale and mx < 142 * scale and my > 1005 * scale and my < 1025 * scale and namestatus == False and gridstatus == False and gstatus == False and bstatus == False:
                    rstatus = True
                elif mx > 142 * scale and mx < 197 * scale and my > 1005 * scale and my < 1025 * scale and namestatus == False and gridstatus == False and rstatus == False and bstatus == False:
                    gstatus = True
                elif mx > 197 * scale and mx < 252 * scale and my > 1005 * scale and my < 1025 * scale and namestatus == False and gridstatus == False and rstatus == False and gstatus == False:
                    bstatus = True
                # + Layer
                elif mx > 350 * scale and mx < 380 * scale and my > 920 * scale and my < 950 * scale:
                    #d = {}
                    layers += 1
                    if selectedlayer == (layers - 1):
                        globals()['imgarr%s' % (selectedlayer + 1)] = numpy.array([[[1.0, 1.0, 1.0 ,0.0] for y in range(imgh)] for z in range(imgw)])
                        globals()['layervis%s' % (selectedlayer + 1)] = True
                    else:
                        for i in range(layers - 1 - selectedlayer):
                            globals()['imgarr%s' % (layers - i)] = globals()['imgarr%s' % (layers - i - 1)]
                            globals()['layervis%s' % (layers - i)] = globals()['layervis%s' % (layers - i - 1)]
                        globals()['imgarr%s' % (selectedlayer + 1)] = numpy.array([[[1.0, 1.0, 1.0 ,0.0] for y in range(imgh)] for z in range(imgw)])
                        globals()['layervis%s' % (selectedlayer + 1)] = True
                # - Layer
                elif mx > 350 * scale and mx < 380 * scale and my > 990 * scale and my < 1020 * scale and layers >= 2:
                    if layers >= 1:
                        if selectedlayer == layers:
                            for i in range(layers - selectedlayer):
                                globals()['imgarr%s' % (selectedlayer + i)] = globals()['imgarr%s' % (selectedlayer + i + 1)]
                                globals()['layervis%s' % (selectedlayer + i)] = globals()['layervis%s' % (selectedlayer + i + 1)]
                            layers -= 1
                            selectedlayer -= 1
                        else:
                            for i in range(layers - selectedlayer):
                                globals()['imgarr%s' % (selectedlayer + i)] = globals()['imgarr%s' % (selectedlayer + i + 1)]
                                globals()['layervis%s' % (selectedlayer + i)] = globals()['layervis%s' % (selectedlayer + i + 1)]
                            layers -= 1
                        if layers - layershift < 6:
                            layershift -= 1
                        if layers <= 6:
                            layershift = 0
                # choose layer
                if mx > 410 * scale and my > 910 * scale and my < 1030 * scale:
                    if mx > 410 * scale and mx < 610 * scale:
                        selectedlayer = 1 + layershift
                    if mx > 630 * scale and mx < 830 * scale and layers >= 2:
                        selectedlayer = 2 + layershift
                    if mx > 850 * scale and mx < 1050 * scale and layers >= 3:
                        selectedlayer = 3 + layershift
                    if mx > 1070 * scale and mx < 1270 * scale and layers >= 4:
                        selectedlayer = 4 + layershift
                    if mx > 1290 * scale and mx < 1490 * scale and layers >= 5:
                        selectedlayer = 5 + layershift
                    if mx > 1510 * scale and mx < 1710 * scale and layers >= 5:
                        selectedlayer = 6 + layershift
                    #animation
                    if mx > 1770 * scale and mx < 1825 * scale and my > 920 * scale and my < 950 * scale:
                        animationstatus = not animationstatus
                    if mx > 1770 * scale and mx < 1825 * scale and my > 990 * scale and my < 1020 * scale:
                        fpsstatus = True

            elif event.button == 3:
                if mx > 410 * scale and my > 910 * scale and my < 1030 * scale:
                    if mx > 410 * scale and mx < 610 * scale:
                        p = 1 + layershift
                        globals()['layervis%s' % p] = not globals()['layervis%s' % p]
                    if mx > 630 * scale and mx < 830 * scale and layers >= 2:
                        p = 2 + layershift
                        globals()['layervis%s' % p] = not globals()['layervis%s' % p]
                    if mx > 850 * scale and mx < 1050 * scale and layers >= 3:
                        p = 3 + layershift
                        globals()['layervis%s' % p] = not globals()['layervis%s' % p]
                    if mx > 1070 * scale and mx < 1270 * scale and layers >= 4:
                        p = 4 + layershift
                        globals()['layervis%s' % p] = not globals()['layervis%s' % p]
                    if mx > 1290 * scale and mx < 1490 * scale and layers >= 5:
                        p = 5 + layershift
                        globals()['layervis%s' % p] = not globals()['layervis%s' % p]
                    if mx > 1510 * scale and mx < 1710 * scale and layers >= 5:
                        p = 6 + layershift
                        globals()['layervis%s' % p] = not globals()['layervis%s' % p]
                elif mx > ((1085 - cw / 2) * scale) + xshift and mx < ((1085 + cw / 2) * scale) + xshift and my > (120 * scale) + yshift and my < ((120 + ch) * scale) + yshift:
                    shiftstatus = True
                    mx2 = mx
                    my2 = my

            elif event.button == 4:
                if mx > 410 * scale and my > 910 * scale and my < 1030 * scale:
                    if layershift > 0:
                        layershift -= 1
                if mx > (1085 - cw / 2) * scale and mx < (1085 + cw / 2) * scale and my > 120 * scale and my < (120 + ch) * scale or mx > 30 * scale and mx < 280 * scale and my > 710 * scale and my < 960 * scale:
                    #zoom = zoom / 1.5
                    None
                    
            elif event.button == 5:
                if mx > 410 * scale and my > 910 * scale and my < 1030 * scale:
                    if layershift + 6 < layers:
                        layershift += 1
                if mx > (1085 - cw / 2) * scale and mx < (1085 + cw / 2) * scale and my > 120 * scale and my < (120 + ch) * scale or mx > 30 * scale and mx < 280 * scale and my > 710 * scale and my < 960 * scale:
                    #zoom = zoom * 1.5
                    None
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mousefunc = False
                fillfunc = True
            if event.button == 3:
                if shiftstatus == True:
                    xshift2 += mx - mx2
                    yshift2 += my - my2
                shiftstatus = False
         
    if mousefunc == True:
        if mx > ((1085 - cw / 2) * scale) + xshift and mx < ((1085 + cw / 2) * scale) + xshift and my > (120 * scale) + yshift and my < ((120 + ch) * scale) + yshift:
            getpixelpos(mx, my)
        elif mx > 30 * scale and mx < 280 * scale and my > 710 * scale and my < 960 * scale:
            color = screen.get_at((mx, my))[:3]
    if animationstatus == True:
        animationcounter += 1
        if animationcounter >= (60 / animationtimer):
            selectedlayer += 1
            animationcounter = 0
        if selectedlayer > layers:
            selectedlayer = 1
    elif namestatus == True and main == True:
        pygame.draw.rect(screen, (255, 0, 0), (720 * scale, 20 * scale, 390 * scale, 20 * scale), 1)
    elif gridstatus == True and main == True:
        if gridpos == 1:
            pygame.draw.rect(screen, (255, 0, 0), (230 * scale, 20 * scale, 50 * scale, 20 * scale), 1)
        else:
            pygame.draw.rect(screen, (255, 0, 0), (260 * scale, 20 * scale, 50 * scale, 20 * scale), 1)
    elif rstatus == True:
        pygame.draw.rect(screen, (255, 0, 0), (87 * scale, 1005 * scale, 55 * scale, 20 * scale), 1)
    elif gstatus == True:
        pygame.draw.rect(screen, (255, 0, 0), (142 * scale, 1005 * scale, 55 * scale, 20 * scale), 1)
    elif bstatus == True:
        pygame.draw.rect(screen, (255, 0, 0), (197 * scale, 1005 * scale, 55 * scale, 20 * scale), 1)
    elif fpsstatus == True:
        pygame.draw.rect(screen, (255, 0, 0), (1765 * scale, 990 * scale, 65 * scale, 30 * scale), 1)
    for i in range(layers):
        if i - layershift <= 5 and i - layershift >= 0 and main == True:
            pygame.draw.rect(screen, (255, 255, 255), ((410 + (220 * (i - layershift)))* scale, 910 * scale, 200 * scale, 120 * scale))
            pygame.draw.rect(screen, (0, 0, 0), ((410 + ( 220 * (i - layershift)))* scale, 910 * scale, 200 * scale, 120 * scale), 3)
            if (i + 1) == selectedlayer:
                pygame.draw.rect(screen, (255, 0, 0), ((410 + ( 220 * (i - layershift)))* scale, 910 * scale, 200 * scale, 120 * scale), 3)
    for i in range(layers):
        if i < 6 and main == True:
            p = i + 1 + layershift
            if globals()['layervis%s' % p] == True:
                layernumbertext = font.render(str(p), 1, (0, 0, 0))
            else:
                layernumbertext = font.render(str(p), 1, (220, 220, 220))
            screen.blit(layernumbertext, ((590 + (220 * i))* scale, 1005 * scale))
            drawcanvas2(imgw, imgh)
    if helpstatus == True and main == True:
        screen.blit(helpbox, (310 * scale, 500 * scale))
        
    if main:
        pygame.display.flip()
        
#undo
#zoom (center mit xshift und y shift machen)
