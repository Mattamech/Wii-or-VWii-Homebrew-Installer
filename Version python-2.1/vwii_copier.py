import os

Program_Location = os.getcwd()

Download_Location = "C:\homebrew"
os.mkdir(Download_Location)
os.chdir(Download_Location)

Save_Location = input("Enter Drive letter (ex G:) here:")
vwii_final = open('vwii_final.bat','w')
vwii_final.write('Xcopy /E /I copy_to_sd ')
vwii_final.write(Save_Location)
vwii_final.close()
os.system('cmd /c vwii_final.bat')
os.system('cmd /c del /f *.bat')


input("If you followed the directions correctly the files should be in the root of the sd card. Press enter to exit.")
exit()