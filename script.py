import pyautogui
import time
import keyboard

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

bm = 0
mbm = 0
skystone = 0


def refresh():
    pyautogui.moveTo(207, 980)
    pyautogui.leftClick()
    time.sleep(1.5)
    pyautogui.moveTo(1092, 656)
    pyautogui.leftClick()
    time.sleep(1.5)


while keyboard.is_pressed("t") == False:
    cov = pyautogui.locateCenterOnScreen(
        "covenant.png", region=(0, 0, 1920, 1080), confidence=0.9
    )
    mystic = pyautogui.locateCenterOnScreen(
        "mystic.png", region=(0, 0, 1920, 1080), confidence=0.9
    )
    if (cov) != None:
        pyautogui.moveTo(cov)
        pyautogui.move(pyautogui.position().x, 10)
        pyautogui.click()
        buyCov2 = pyautogui.locateCenterOnScreen(
            "buyCov2.png", region=(0, 0, 1920, 1080), confidence=0.9
        )
        pyautogui.moveTo(buyCov2)
        pyautogui.click()
        bm += 1

    if (mystic) != None:
        pyautogui.moveTo(mystic)
        pyautogui.move(pyautogui.position().x, 10)
        pyautogui.click()
        mysticConfirm = pyautogui.locateCenterOnScreen(
            "mysticConfirm.png", region=(0, 0, 1920, 1080), confidence=0.8
        )
        pyautogui.moveTo(mysticConfirm)
        pyautogui.click()
        mbm += 1
    time.sleep(1.5)
    pyautogui.scroll(-2)
    time.sleep(1)
    cov = pyautogui.locateCenterOnScreen(
        "covenant.png", region=(0, 0, 1920, 1080), confidence=0.9
    )
    mystic = pyautogui.locateCenterOnScreen(
        "mystic.png", region=(0, 0, 1920, 1080), confidence=0.9
    )
    if (cov) != None:
        pyautogui.moveTo(cov)
        pyautogui.move(pyautogui.position().x, 10)
        pyautogui.click()
        buyCov2 = pyautogui.locateCenterOnScreen(
            "buyCov2.png", region=(0, 0, 1920, 1080), confidence=0.9
        )
        pyautogui.moveTo(buyCov2)
        pyautogui.click()
        bm += 1

    if (mystic) != None:
        pyautogui.moveTo(mystic)
        pyautogui.move(pyautogui.position().x, 10)
        pyautogui.click()
        mysticConfirm = pyautogui.locateCenterOnScreen(
            "mysticConfirm.png", region=(0, 0, 1920, 1080), confidence=0.8
        )
        pyautogui.moveTo(mysticConfirm)
        pyautogui.click()
        mbm += 1
    refresh()
    skystone += 3

print(f"Covenant bookmarks: {bm}")
print(f"Mystic Bookmarks: {mbm}")
print(f"Skystones: {skystone}")
