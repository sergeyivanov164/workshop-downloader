import os
import time
import shutil

userLanguage = input("Язык/language (ru/en): ")

if (userLanguage == "ru"):
    gameId = input("Введите ID игры: ")
    downloadPatch = input("Введите путь скачивания: ")
    while True:
        modId = input("Введите ID мода (или cancel для отмены): ")
        if (modId == "cancel"): exit()
        command = f"steamcmd +login anonymous +workshop_download_item {gameId} {modId} +quit"
        os.chdir("\workshop-downloader\SteamCMD")
        os.system(command)
        print()
        workingDir = os.getcwd()
        shutil.move(f"{workingDir}\steamapps\workshop\content\{gameId}\{modId}", downloadPatch)
        print("Выполнено")

elif (userLanguage == "en"):
    gameId = input("Enter game ID: ")
    downloadPatch = input("Enter download path: ")
    while True:
        modId = input("Enter mod ID (or cancel to cancel): ")
        if (modId == "cancel"): exit()
        command = f"steamcmd +login anonymous +workshop_download_item {gameId} {modId} +quit"
        os.chdir("\workshop-downloader\SteamCMD")
        os.system(command)
        print()
        workingDir = os.getcwd()
        shutil.move(f"{workingDir}\steamapps\workshop\content\{gameId}\{modId}", downloadPatch)
        print("Done")


else:
    print("Error")
    time.sleep(2)
    exit()
