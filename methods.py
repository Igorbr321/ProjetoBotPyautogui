import pyautogui
import numpy as np
from PIL import ImageGrab
import time

def changeWindow():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

# Coordenada: local de pesca
def fishingSpot():
    time.sleep(.1)
    pyautogui.moveTo(1111, 678)
    time.sleep(.1)
    pyautogui.click(1111, 678)

# Coordenada: local de ataque ao pokemon (battle)
def attackPokemonSpot():
    time.sleep(1)
    pyautogui.moveTo(1745, 310)
    time.sleep(.1)
    pyautogui.click(1745, 310)

# Coordenada: local que o pokemon morreu (abrir loot)
def openLoot():
    time.sleep(.1)
    pyautogui.moveTo(1036, 454)
    time.sleep(.1)
    pyautogui.rightClick(1036, 454)

def pokemonSpot():
    time.sleep(.1)
    pyautogui.moveTo(1036, 454)
    time.sleep(.1)
    pyautogui.click(1036, 454)

# Coordenada: primeiro espaço do loot do pokemon (coletar loot)
def takeLoot():
    time.sleep(.1)
    pyautogui.moveTo(1743, 659)
    time.sleep(.1)
    pyautogui.rightClick(1743, 659)
    time.sleep(.1)
    pyautogui.rightClick(1743, 659)
    time.sleep(.1)
    pyautogui.rightClick(1743, 659)
    time.sleep(.1)
    pyautogui.rightClick(1743, 659)

# Coordenada: fechar aba de loot do pokemon
def closeLoot():
    time.sleep(.1)
    pyautogui.moveTo(1903, 638)
    time.sleep(.1)
    pyautogui.click(1903, 638)

# Ordem de habilidades
def skillOrder(a,b,c,d,e,f,g,h,i,j):
    time.sleep(.1)
    pyautogui.press(a)
    time.sleep(.1)
    pyautogui.press(b)
    time.sleep(.1)
    pyautogui.press(c)
    time.sleep(.1)
    pyautogui.press(d)
    time.sleep(.1)
    pyautogui.press(e)
    time.sleep(.1)
    pyautogui.press(f)
    time.sleep(.1)
    pyautogui.press(g)
    time.sleep(.1)
    pyautogui.press(h)
    time.sleep(.1)
    pyautogui.press(i)
    time.sleep(.1)
    pyautogui.press(j)

# Ação: usar skill Safeguard
def useSkillSafeGuard():
    time.sleep(.1)
    pyautogui.press('f1')

# Ação: pescar
def toFish():
    time.sleep(.1)
    pyautogui.keyDown('shift')
    time.sleep(.1)
    pyautogui.press('f1')
    time.sleep(.1)
    pyautogui.keyUp('shift')
    
    fishingSpot()

# Peixe encontrado
def catchTheFish():
    toFish()     
    fishingSpot()   

# Ação: user pokeball
def usePokeball():
    time.sleep(.1)
    pyautogui.keyDown('shift')
    time.sleep(.1)
    pyautogui.press('f6')
    time.sleep(.1)
    pyautogui.keyUp('shift')
    pokemonSpot()
