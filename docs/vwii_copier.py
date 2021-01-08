import os

Program_Location = os.getcwd()

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


rerun = input("Do you wish to [1]rerun the script,\n[2]delete the copy-to-sd folder,\n[3]or just exit?\nEnter the number that matches your choice.\n")
if rerun == "1":
    os.chdir(Program_Location)
    os.system('cmd /c py vwii_copier.py')
    exit()
elif rerun == "2":
    os.chdir(Program_Location)
    delete = open('Delete.bat','w')
    delete.write('RD /S /Q ')
    delete.write(Download_Location)
    delete.close()
    os.system('cmd /c Delete.bat')
    os.system('cmd /c del /f Delete.bat')
    exit()
elif rerun == "3":
    exit()
else:
    input("Whoops! That wasn't supposed to happen! Press enter to exit.")
    exit()