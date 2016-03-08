import pyautogui
import random

print('Place your cursor on the first bone.')

numBones = int(input('How many bones do you have?'))

column = 1

if numBones is not 28:
    column = int(input('In which inventory column is your first bone?'))

interval = .95

pyautogui.click()

for i in range(numBones - 1):
    interval = random.uniform(.95, 1)

    if column is 4:
        pyautogui.moveRel(-120, 37, duration=interval)
        column = 1
    else:
        pyautogui.moveRel(40, 0, duration=interval)
        column += 1

    pyautogui.click()
