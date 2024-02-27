import os 
import keyboard
def hotkey_pressed():
    os.system("taskkill /f /im chrome.exe")
    # os.system("taskkill /f /im code.exe")
    # os.system("taskkill /f /im msedge.exe") 
    os.system("taskkill /f /im vivaldi.exe") 
    

keyboard.add_hotkey('shift', hotkey_pressed)
keyboard.wait() 
# response = os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk")
# os.system("taskkill /f /im chrome.exe")
# os.system("taskkill /f /im code.exe")
# os.system("taskkill /f /im msedge.exe") 
# os.system("taskkill /f /im mongod.exe")
 