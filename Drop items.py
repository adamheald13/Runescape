import pyautogui

interval = .001


class Drop:
    def dropItems(self):
        pyautogui.rightClick()
        pyautogui.moveRel(0, 40)
        pyautogui.click()
        pyautogui.moveRel(0, -40)

drop = Drop()

print('Place your cursor on the first item to drop.')

numBones = int(input('How many items do you have that you wish to drop?'))

column = 1

if numBones is not 24:
    column = int(input('In which inventory column is the first item to drop?'))

drop.dropItems()

for i in range(numBones - 1):

    if column is 4:
        pyautogui.moveRel(-120, 37)
        column = 1
    else:
        pyautogui.moveRel(40, 0)
        column += 1

    drop.dropItems()
