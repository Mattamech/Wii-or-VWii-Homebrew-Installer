# Made by Lord-Giganticus
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