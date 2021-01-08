import os

Download_Location = input("Enter folder with downloaded files here:")
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

input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()