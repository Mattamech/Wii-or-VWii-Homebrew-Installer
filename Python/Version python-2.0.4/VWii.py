import os
import shutil

Download_Location = input("Enter folder here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

vwii_downloader = open('vwii_downloader.bat','w')
vwii_downloader.write('curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip\ncurl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/hackmii_installer_v1.2.1.zip -o hackmii_installer_v1.2.zip\ncurl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/wuphax.zip -o wuphax.zip\ncurl http://stahlworks.com/dev/unzip.exe --output unzip.exe')
vwii_downloader.close()

input("Double Check that vwii_downloader.bat is now in the folder you specifyed. Press enter to continue.")

os.system('cmd /c vwii_downloader.bat')
os.system('cmd /c unzip *.zip')
os.system('cmd /c del /f *.zip')
os.system('cmd /c del /f *.txt')
os.system('cmd /c del /f *.exe')
os.system('cmd /c del /f *.bat')
vwii_copier = open('vwii_copier.bat','w')
vwii_copier.write('mkdir apps\ncd apps\nmkdir homebrew_browser\ncd ../\nXcopy /E /I homebrew_browser apps\homebrew_browser\nRD /S /Q homebrew_browser')
vwii_copier.close()
os.system('cmd /c vwii_copier.bat')
os.system('cmd /c del /f *.bat')
os.system('cmd /c del /f *.install')
os.system('cmd /c del /f *.json')
os.system('cmd /c RD /S /Q "Homebrew Browser Guide and Help"')

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

input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()