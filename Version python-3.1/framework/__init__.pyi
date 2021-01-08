# Made by Lord-Giganticus and Mattamech. Please do not repost this without crediting us! :)

Version = 3

import os
import shutil

class error:
    def problem(x:int, y:int):
        if y == 0:
            print("There was a input error on line",str(x)+'.')
        elif y != 0 and y > 0:
            print('There was a error somewhere between line',str(x),'and line',str(y)+'.')
        elif y != 0 and y < 0:
            print('y is less than 0! It is set to',str(y),'and x is set to',str(x)+'. Please inform the author that this has occured!')
        input('Press enter to exit.')
        exit()

class main:
    def wii():
        try:
            Download_Location = input("Enter folder here:")
            os.chdir(Download_Location)
            print(os.getcwd())
            input("If the folder above is not correct you will have to restart. Press enter to continue.")

            wii_downloader = open('wii_downloader.bat','w')
            wii_downloader.write('curl https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip --output homebrew_browser.zip\n')
            wii_downloader.write('curl https://wii.guide/assets/files/Priiloader_v0_8_2.zip --output Priiloader.zip\n')
            wii_downloader.write('curl https://mattamech.github.io/Wii-or-VWii-Homebrew-Installer/docs/hackmii_installer_v1.2.1.zip -o hackmii_installer_v1.2.zip\n')
            wii_downloader.write('curl http://stahlworks.com/dev/unzip.exe --output unzip.exe')
            wii_downloader.close()

            os.system('cmd /c wii_downloader.bat')
            os.system('cmd /c unzip *.zip')
            os.system('cmd /c del /f *.zip')
            os.system('cmd /c del /f *.txt')
            os.system('cmd /c del /f *.exe')
            os.system('cmd /c del /f *.bat')
            wii_copier = open('wii_copier.bat','w')
            wii_copier.write('cd apps\n')
            wii_copier.write('mkdir homebrew_browser\n')
            wii_copier.write('cd ../\n')
            wii_copier.write('Xcopy /E /I homebrew_browser apps\homebrew_browser\n')
            wii_copier.write('RD /S /Q homebrew_browser')
            wii_copier.close()
            os.system('cmd /c wii_copier.bat')
            os.system('cmd /c del /f *.bat')
            os.system('cmd /c RD /S /Q "Homebrew Browser Guide and Help"')

            if os.path.isdir('copy_to_sd') == True:
                os.chdir('copy_to_sd')
                os.system('cmd /c RD /S /Q apps')
                os.system('cmd /c RD /S /Q extra')
                os.chdir(Download_Location)
                shutil.copyfile('boot.elf', 'copy_to_sd/boot.elf')
                shutil.copyfile('bootmini.elf', 'copy_to_sd/bootmini.elf')
                shutil.copytree('apps', 'copy_to_sd/apps')
                shutil.copytree('extra', 'copy_to_sd/extra')
            else:
                os.mkdir('copy_to_sd')
                shutil.copyfile('boot.elf', 'copy_to_sd/boot.elf')
                shutil.copyfile('bootmini.elf', 'copy_to_sd/bootmini.elf')
                shutil.copytree('apps', 'copy_to_sd/apps')
                shutil.copytree('extra', 'copy_to_sd/extra')

            Save_Location = input("Enter drive letter (EX: G:) here:")
            wii_final = open('wii_final.bat','w')
            wii_final.write('Xcopy /E /I copy_to_sd ')
            wii_final.write(Save_Location)
            wii_final.close()
            os.system('cmd /c wii_final.bat')
            os.system('cmd /c RD /S /Q apps')
            os.system('cmd /c RD /S /Q extra')
            os.system('cmd /c del /f *.elf')
            os.system('cmd /c del /f *.bat')
        except:
            error.problem(22, 76)

    def wii_copier():
        try:
            Download_Location = input("Enter folder here:")
            os.chdir(Download_Location)
            print(os.getcwd())
            input("If the folder above is not correct you will have to restart. Press enter to continue.")

            Save_Location = input("Enter Drive letter (ex G:) here:")
            wii_final = open('wii_final.bat','w')
            wii_final.write('Xcopy /E /I copy_to_sd ')
            wii_final.write(Save_Location)
            wii_final.close()
            os.system('cmd /c wii_final.bat')
            os.system('cmd /c del /f *.elf')
            os.system('cmd /c del /f *.bat')
        except:
            error.problem(81, 94)

    def vwii():
        try:
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
        except:
            error.problem(100, 173)

    def vwii_copier():
        try:
            Download_Location = input("Enter folder here:")
            os.chdir(Download_Location)
            print(os.getcwd())
            input("If the folder above is not correct you will have to restart. Press enter to continue.")

            Save_Location = input("Enter Drive letter (ex G:) here:")
            vwii_final = open('vwii_final.bat','w')
            vwii_final.write('Xcopy /E /I copy_to_sd ')
            vwii_final.write(Save_Location)
            vwii_final.close()
            os.system('cmd /c vwii_final.bat')
            os.system('cmd /c del /f *.bat')
        except:
            error.problem(179, 190)

def complete():
    input("Complete. Press enter to exit.")

print("framework all setup and ready to go.")