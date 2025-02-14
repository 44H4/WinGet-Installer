import os
from colorama import Fore, init



# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + """

██╗    ██╗██╗███╗   ██╗ ██████╗ ███████╗████████╗    ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
██║    ██║██║████╗  ██║██╔════╝ ██╔════╝╚══██╔══╝    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║██║  ███╗█████╗     ██║       ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║██║   ██║██╔══╝     ██║       ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║╚██████╔╝███████╗   ██║       ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                           
""")

print(Fore.CYAN + "If the WINGET INSTALLER logo is not displayed correctly, please make the terminal window fullscreen. If there are any other issues, please report them to the developer at \x1b]8;;http://github.com/44H4/WinGet-Installer/issues/\x1b\\the GitHub page\x1b]8;;\x1b\\.")

print(Fore.CYAN + "Welcome to the The Winget Hub Installer")

print(Fore.CYAN + "developed by: \x1b]8;;http://github.com/44H4/\x1b\\44H4\x1b]8;;\x1b\\.")

print(Fore.CYAN + "\nPlease choose the program you want to install:")

print(Fore.CYAN + """
Package Options:
      
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

Games:

    13. Steam
    14. Epic Games Store
    15. GeForce Now
    16. EA App

Development Tools:

    17. Visual Studio Code
    18. Git
    19. GitHub Desktop
    20. JetBrains Toolbox
    21. GitHub CLI
    22. Node.js

Communications/Social Media:
      
    23. Discord
    24. Slack
    25. Microsoft Teams
    26. Zoom
    27. Skype
    28. WhatsApp
    29. Telegram
    30. Signal
    31. Twitter
    32. Instagram
    33. Facebook
      """)

programRequest = input(Fore.CYAN + "Enter the name or number of the program you want to install: ")

if programRequest == "1, Chrome, Google Chrome":
    os.system("winget install --id Google.Chrome")
if programRequest == "2, Firefox, Mozilla Firefox":
    os.system("winget install --id Mozilla.Firefox")
if programRequest == "3, Opera, Opera Browser":
    os.system("winget install --id Opera.Opera")
if programRequest == "4, Brave, Brave Browser":
    os.system("winget install --id BraveSoftware.BraveBrowser")
if programRequest == "5, Vivaldi, Vivaldi Browser":
    os.system("winget install --id VivaldiTechnologies.Vivaldi")
if programRequest == "6, Tor, Tor Browser":
    os.system("winget install --id TheTorProject.TorBrowser")
if programRequest == "7, 7-Zip, 7Zip":
    os.system("winget install --id 7zip.7zip")
if programRequest == "8, WinRAR, Win RAR":
    os.system("winget install --id RarLab.WinRAR")
if programRequest == "9, Notepad++, Notepad ++, Notepad":
    os.system("winget install --id Notepad++.Notepad++")
if programRequest == "10, VLC, VLC Media Player":
    os.system("winget install --id VideoLAN.VLC")
if programRequest == "11, Python, Python 3, Python3":
    os.system("winget install --id Python.Python")
if programRequest == "12, Spotify, Spotify Music":
    os.system("winget install --id Spotify.Spotify")

if programRequest == "13, Steam":
    os.system("winget install --id Valve.Steam")
if programRequest == "14, Epic Games, Epic Games Store":
    os.system("winget install --id EpicGames.EpicGamesStore")
if programRequest == "15, GeForce Now, GeForceNow":
    os.system("winget install --id NVIDIA.GeforceNow")
if programRequest == "16, EA, EA App":
    os.system("winget install --id ElectronicArts.EAApp")
if programRequest == "17, Visual Studio Code, VS Code":
    os.system("winget install --id Microsoft.VisualStudioCode")
if programRequest == "18, Git":
    os.system("winget install --id Git.Git")
if programRequest == "19, GitHub Desktop":
    os.system("winget install --id GitHub.GitHubDesktop")
if programRequest == "20, JetBrains Toolbox":
    os.system("winget install --id JetBrains.Toolbox")
if programRequest == "21, GitHub CLI":
    os.system("winget install --id GitHub.cli")
if programRequest == "22, Node.js, Node":
    os.system("winget install --id OpenJS.NodeJS")
if programRequest == "23, Discord":
    os.system("winget install --id Discord.Discord")
if programRequest == "24, Slack":
    os.system("winget install --id SlackTechnologies.Slack")
if programRequest == "25, Microsoft Teams, Teams":
    os.system("winget install --id Microsoft.Teams")
if programRequest == "26, Zoom":
    os.system("winget install --id Zoom.Zoom")    
if programRequest == "27, Skype":
    os.system("winget install --id Skype.Skype")
if programRequest == "28, WhatsApp":
    os.system("winget install --id WhatsApp.WhatsApp")
if programRequest == "29, Telegram":
    os.system("winget install --id Telegram.TelegramDesktop")
if programRequest == "30, Signal":
    os.system("winget install --id Signal.Signal")
if programRequest == "31, Twitter":
    os.system("winget install --id Twitter.Twitter")
if programRequest == "32, Instagram":
    os.system("winget install --id Instagram.Instagram")
if programRequest == "33, Facebook":
    os.system("winget install --id Facebook.Facebook")

else:
    print(Fore.RED + "Invalid input. Please try again. If there is a bug, please report it to the developer at \x1b]8;;http://github.com/44H4/WinGet-Installer/issues/\x1b\\the GitHub page\x1b]8;;\x1b\\.")

input(Fore.RED + "Press Enter to exit...")