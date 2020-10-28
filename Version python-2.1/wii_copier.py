import os

Program_Location = os.getcwd()

Download_Location = "C:\homebrew"
os.mkdir(Download_Location)
os.chdir(Download_Location)

Save_Location = input("Enter Drive letter (ex G:) here:")
wii_final = open('wii_final.bat','w')
wii_final.write('Xcopy /E /I copy_to_sd ')
wii_final.write(Save_Location)
wii_final.close()
os.system('cmd /c wii_final.bat')
os.system('cmd /c del /f *.elf')
os.system('cmd /c del /f *.bat')

input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()