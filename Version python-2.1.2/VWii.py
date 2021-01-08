# Made by Lord-Giganticus and Mattamech. Please do not repost this without crediting us! :)

# Version 2.1.2

import os
import shutil

Program_Location = os.getcwd()

Download_Location = input("Enter folder here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

vwii_downloader = open('vwii_downloader.bat','w')
vwii_downloader.write('curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip\n')
vwii_downloader.write('curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/hackmii_installer_v1.2.1.zip -o hackmii_installer_v1.2.zip\n')
vwii_downloader.write('curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/wuphax.zip -o wuphax.zip\n')
vwii_downloader.write('curl http://stahlworks.com/dev/unzip.exe --output unzip.exe')
vwii_downloader.close()

input("Double Check that vwii_downloader.bat is now in the folder you specifyed. Press enter to continue.")

os.system('cmd /c vwii_downloader.bat')
os.system('cmd /c unzip *.zip')
os.system('cmd /c del /f *.zip')
os.system('cmd /c del /f *.txt')
os.system('cmd /c del /f *.exe')
os.system('cmd /c del /f *.bat')

if os.path.isdir('apps') == True:
    vwii_copier = open('vwii_copier.bat','w')
    vwii_copier.write('cd apps\n')
    vwii_copier.write('mkdir homebrew_browser\n')
    vwii_copier.write('cd ../\n')
    vwii_copier.write('Xcopy /E /I homebrew_browser apps\homebrew_browser\n')
    vwii_copier.write('RD /S /Q homebrew_browser')
    vwii_copier.close()
else:
    vwii_copier = open('vwii_copier.bat','w')
    vwii_copier.write('mkdir apps\n')
    vwii_copier.write('cd apps\n')
    vwii_copier.write('mkdir homebrew_browser\n')
    vwii_copier.write('cd ../\n')
    vwii_copier.write('Xcopy /E /I homebrew_browser apps\homebrew_browser\n')
    vwii_copier.write('RD /S /Q homebrew_browser')
    vwii_copier.close()


os.system('cmd /c vwii_copier.bat')
os.system('cmd /c del /f *.bat')
os.system('cmd /c del /f *.install')
os.system('cmd /c del /f *.json')
os.system('cmd /c RD /S /Q "Homebrew Browser Guide and Help"')

if os.path.isdir('copy_to_sd') == True:
    os.chdir('copy_to_sd')
    os.system('cmd /c RD /S /Q apps')
    os.system('cmd /c RD /S /Q wiiu')
    os.system('cmd /c del /f *.elf')
    os.system('cmd /c del /f *.bat')
    os.chdir(Download_Location)
    shutil.copyfile('boot.elf', 'copy_to_sd/boot.elf')
    shutil.copyfile('bootmini.elf', 'copy_to_sd/bootmini.elf')
    shutil.copytree('apps', 'copy_to_sd/apps')
    shutil.copytree('wiiu', 'copy_to_sd/wiiu')
else:
    os.mkdir('copy_to_sd')
    shutil.copyfile('boot.elf', 'copy_to_sd/boot.elf')
    shutil.copyfile('bootmini.elf', 'copy_to_sd/bootmini.elf')
    shutil.copytree('apps', 'copy_to_sd/apps')
    shutil.copytree('wiiu', 'copy_to_sd/wiiu')

Save_Location = input("Enter Drive letter (ex G:) here:")
vwii_final = open('vwii_final.bat','w')
vwii_final.write('Xcopy /E /I copy_to_sd ')
vwii_final.write(Save_Location)
vwii_final.close()
os.system('cmd /c vwii_final.bat')
os.system('cmd /c RD /S /Q apps')
os.system('cmd /c RD /S /Q wiiu')
os.system('cmd /c del /f *.elf')
os.system('cmd /c del /f *.bat')

run_copier = input("Do you wish to\n[1]run the copier,\n [2]delete the copy-to-sd folder,\n [3]or just exit?\n Enter a number to shown to choose.\n")
if run_copier == "1":
    os.chdir(Program_Location)
    os.system('cmd /c curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/python/vwii_copier.py -o wii_copier.py')
    os.system('cmd /c py wii_copier.py')
    exit()
elif run_copier == "2":
    os.system('cmd /c RD /S /Q copy_to_sd')
    exit()
elif run_copier == "3":
    exit()
else:
    input("Whoops! That wasn't supposed to happen! Press enter to exit.")
    exit()