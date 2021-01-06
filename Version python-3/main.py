# Made by Lord-Giganticus and Mattamech. Please do not repost this without crediting us! :)

import framework

option = int(input("Enter the number corresponding to which one of the py files you wish to run:\n[1]vwii.py\n[2]vwii_copier.py\n[3]wii.py\n[4]wii_copier.py"))
if option == 1:
    framework.vwii()
    framework.complete()
elif option == 2:
    framework.vwii_copier()
    framework.complete()
elif option == 3:
    framework.wii()
    framework.complete()
elif option == 4:
    framework.wii_copier()
    framework.complete()
else:
    input("You didn't input one of the numbers allowed! Press enter to exit.")
    exit()