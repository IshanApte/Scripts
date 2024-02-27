import os 
import keyboard
def hotkey_pressed():
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im code.exe")
    os.system("taskkill /f /im msedge.exe") 
    os.system("taskkill /f /im vivaldi.exe") 
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk")
    
# def do_work():
#     os.system("taskkill /f /im C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk")
#     os.startfile("C:\Users\ishan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")

keyboard.add_hotkey('alt+v', hotkey_pressed)
# keyboard.add_hotkey('alt+d', do_work)
keyboard.wait() 
