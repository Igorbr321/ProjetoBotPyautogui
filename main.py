import pyautogui
import numpy as np
from PIL import ImageGrab
import time
import methods

pyautogui.PAUSE = 0.2

pyautogui.alert('BOT Online ( ͡≖ ͜ʖ ͡≖)')

methods.changeWindow()

looping = True

while looping == True:

    methods.useSkillSafeGuard()
    methods.toFish()

    search = True
    isFished = False

    while search == True: 
        try:
            if (
                pyautogui.locateCenterOnScreen(
                        'peixe.png'
                    )
                ):
                methods.catchTheFish()
                search = False
                isFished = True    
        except:
            time.sleep(1)
            print("Não foi possível pescar o pokemon")


    if (isFished == True):

        methods.useSkillSafeGuard() 
        methods.attackPokemonSpot()
        methods.skillOrder(
            'f1',
            'f2',
            'f4',
            'f3',
            'f5',
            'f6',
            'f7',
            'f8',
            'f9',
            'f10',
        )
        time.sleep(1)
        if not (
            pyautogui.locateCenterOnScreen(
                    'nothing.png'
                )
            ):  
            methods.openLoot()
            methods.takeLoot()
            methods.closeLoot()

        methods.usePokeball()

    else:
        pyautogui.alert('ERROR')