import os
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Set console to fullscreen
os.system("powershell -command \"[console]::WindowWidth = [console]::LargestWindowWidth; [console]::WindowHeight = [console]::LargestWindowHeight\"")

print(Fore.CYAN + """
██╗    ██╗██╗███╗   ██╗ ██████╗ ███████╗████████╗    ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
██║    ██║██║████╗  ██║██╔════╝ ██╔════╝╚══██╔══╝    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║██║  ███╗█████╗     ██║       ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║██║   ██║██╔══╝     ██║       ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║╚██████╔╝███████╗   ██║       ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
""")
print(Fore.CYAN + "Welcome to the The Winget Hub Installer")

print(Fore.CYAN + "developed by: \x1b]8;;http://github.com/44H4/'\x1b\\44H4\x1b]8;;\x1b\\.")

print(Fore.CYAN + "\nPlease choose the program you want to install:")

print(Fore.CYAN + """
Browsers:
1. Chrome Browser
2. Firefox Browser
3. Opera Browser
4. Brave Browser
5. Vivaldi Browser
6. Tor Browser
Utilities:
7. 7-Zip
8. WinRAR
9. Notepad++
10. VLC Media Player
11. Python
12. Spotify
""")

programRequest = input(Fore.CYAN + "Enter the number of the program you want to install: ")

if programRequest == "1":
    os.system("winget install --id Google.Chrome")
if programRequest == "2":
    os.system("winget install --id Mozilla.Firefox")
if programRequest == "3":
    os.system("winget install --id Opera.Opera")
if programRequest == "4":
    os.system("winget install --id BraveSoftware.BraveBrowser")
if programRequest == "5":
    os.system("winget install --id VivaldiTechnologies.Vivaldi")
if programRequest == "6":
    os.system("winget install --id TheTorProject.TorBrowser")
if programRequest == "7":
    os.system("winget install --id 7zip.7zip")
if programRequest == "8":
    os.system("winget install --id RarLab.WinRAR")
if programRequest == "9":
    os.system("winget install --id NotepadPlusPlus.NotepadPlusPlus")
if programRequest == "10":
    os.system("winget install --id VideoLAN.VLC")
if programRequest == "11":
    os.system("winget install --id Python.Python")
if programRequest == "12":
    os.system("winget install --id Spotify.Spotify")
else:
    print(Fore.CYAN + "Invalid input. Please try again with the numbers 1-12. If there is a bug, please report it to the developer at \x1b]8;;http://github.com/44H4/WinGet-Installer/issues/\x1b\\ the GitHub page\x1b]8;;\x1b\\.")

input(Fore.CYAN + "Press Enter to exit...")