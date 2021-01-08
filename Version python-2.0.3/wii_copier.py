import os

Download_Location = input("Enter folder with downloaded files here:")
os.chdir(Download_Location)
print(os.getcwd())
input("If the folder above is not correct you will have to restart. Press enter to continue.")

if os.path.isdir('copy_to_sd') == False:
    input("copy_to_sd does not exist here! Press enter to exit and next time, enter the correct folder.")
    exit()

Save_Location = input("Enter Drive letter (ex G:) here:")
wii_final = open('wii_final.bat','w')
wii_final.write('Xcopy /E /I copy_to_sd ')
wii_final.write(Save_Location)
wii_final.close()
os.system('cmd /c wii_final.bat')
os.system('cmd /c del /f *.elf')
os.system('cmd /c del /f *.bat')

rerun = input("Do you wish to\n[1]rerun the script,\n[2]delete the copy-to-sd folder,\n[3]or just exit?\nEnter the number that matches your choice.\n")
if rerun == "1":
    os.system('cmd /c py wii_copier.py')
    exit()
elif rerun == "2":
    os.system('cmd /c RD /S /Q copy_to_sd')
    exit()
elif rerun == "3":
    exit()
else:
    input("Whoops! That wasn't supposed to happen! Press enter to exit.")
    exit()