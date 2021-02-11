# Made by Lord-Giganticus and Mattamech. Please do not repost this without crediting us! :)

from framework import core, complete
option = int(input("Enter the number corresponding to which one of the py files you wish to run:\n[1]vwii.py\n[2]vwii_copier.py\n[3]wii.py\n[4]wii_copier.py\n"))
if option == 1:
    core.vwii()
    complete()
elif option == 2:
    core.vwii_copier()
    complete()
elif option == 3:
    core.wii()
    complete()
elif option == 4:
    core.wii_copier()
    complete()
else:
    input("You didn't input one of the numbers allowed! Press enter to exit.")
    exit()