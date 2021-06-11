import pyautogui
import webbrowser

webbrowser.open("https://gshow.globo.com/realities/bbb/bbb21/votacao/paredao-bbb21-vote-para-eliminar-arthur-gilberto-ou-karol-conka-838ec4d5-7d17-4263-a335-29e13c3a769b.ghtml")

i = 0

while i < 1:
    pyautogui.moveTo(1250,800,duration = 1.5)
    pyautogui.click()
    pyautogui.moveTo(1180,1000, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(1180,450, duration = 1)
    pyautogui.click()
    i += 1