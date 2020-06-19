import wget
from shutil import copyfile
import os
import shutil

Download_Location = input("Enter folder here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

wget.download('https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/vwii_downloader.bat', 'vwii_downloader.bat')

clear = lambda: os.system('cls')
clear()

input("Double Check that vwii_downloader.bat is now in the folder you specifyed. Press enter to continue.")

os.system('cmd /c vwii_downloader.bat')
os.system('cmd /c unzip *.zip')
os.system('cmd /c del /f *.zip')
os.system('cmd /c del /f *.txt')
os.system('cmd /c del /f *.exe')
wget.download('https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/vwii_copier.bat', 'vwii_copier.bat')
os.system('cmd /c vwii_copier.bat')
os.system('cmd /c del /f *.bat')
os.system('cmd /c del /f *.install')
os.system('cmd /c del /f *.json')
os.system('cmd /c RD /S /Q "Homebrew Browser Guide and Help"')

os.mkdir('copy_to_sd')
shutil.move('boot.elf', 'copy_to_sd')
shutil.move('bootmini.elf', 'copy_to_sd')
shutil.copytree('apps', 'copy_to_sd/apps')
shutil.copytree('wiiu', 'copy_to_sd/wiiu')

Save_Location = input("Enter Drive letter (ex G:) here:")
shutil.move('copy_to_sd/boot.elf', Save_Location)
shutil.move('copy_to_sd/bootmini.elf', Save_Location)
shutil.move('copy_to_sd/apps', Save_Location)
shutil.move('copy_to_sd/wiiu', Save_Location)


input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()