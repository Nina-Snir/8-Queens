#ako rozloziť 8 dám na sachovnici aby sa navzájom neohrozovali
#TODO princíp = prechadzat a checkovať
import numpy as np
from PIL import Image, ImageDraw
import os

directory = "riesenia"
parent_dir = "C:/Users/Nina/PycharmProjects/Hodina 4.11 - Rekurzia"
path = os.path.join(parent_dir,directory)
os.mkdir(path)


sirka = 8
sachovnica = []

def creator(sirka = 8): #vytvori sachovnicu
    global sachovnica
    sachovnica = np.zeros((sirka,sirka),dtype = int)

def check(x:int,y:int) ->bool:
    sucet = x+y
    rozdiel = x-y
    for xova in range(sirka):
        for yova in range(sirka):
            if xova ==x or yova==y or xova+yova ==sucet or xova-yova==rozdiel:
                if sachovnica[xova][yova] == 1:
                    return False
    return True
count= 1
def attack(cd = 0):
    global sachovnica
    global count

    if cd == 8:
        #img= f"img_{count}"
        img = Image.new("RGB", (640, 640), "white")  # create a new 15x15 image
        draw = ImageDraw.Draw(img)
        pixels = img.load()  # create the pixel map
        bl = True
        for i in range(0,640,80):
            for j in range(0,640,80):
                if bl==True:
                    draw = ImageDraw.Draw(img)
                    draw.rectangle([(i,j),(i+80,j+80)],fill = "black")
                    bl = False
                else:
                    draw = ImageDraw.Draw(img)
                    draw.rectangle([(i,j),(i+80,j+80)], fill="white")
                    bl= True
            if bl == True:
                bl = False
            else:
                bl = True #sachovnicu by sme mali
        for i in range(8):
            for j in range(8):
                if sachovnica[i][j] == 1:
                    posx = i*80
                    posy = j*80
                    draw.ellipse([(posx,posy),(posx+80,posy+80)],fill = "red")
        img_path = "C:/Users/Nina/PycharmProjects/Hodina 4.11 - Rekurzia"
        img.save(f"{img_path}/riesenia/{count}.png")

        count+=1
    else:
        for i in range(sirka):
            if check(cd,i):
                sachovnica[cd][i] = 1
                attack(cd+1)
                sachovnica[cd][i] = 0
creator()
print(sachovnica)
attack(0)




#TODO - dokonceny check v utorok

#TODO  - modofikovat program tak, aby riesenia nevypisoval do command line ale aby vytvoril adresar
# riesenia a za kazde riesenie vytvoril obrazok typu png/jpg na ktorom bude dana situacia zobrazena
# zavolas PIL (finkcia draw) - transparentne pozadie
#TODO  - vytvorit adresa a donho ukladat



