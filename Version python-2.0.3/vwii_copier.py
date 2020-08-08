import shutil
import os

Download_Location = input("Enter folder with downloaded files here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

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