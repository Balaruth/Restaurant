# coding=utf-8
menu = {}

print "Welcome to the menu generator!"
print
add = True # Will loop adding to the menu until user declines
while add == True:
  food = raw_input("Please enter a dish for today's menu: ")
  price = raw_input("And how much does this dish cost? ")

  try:
    price = float(price) # If price entered is not a number it will be rejected
    price = str('%.2f' % price) # Display price with 2 decimal places
    menu[food] = price

    validation = True
    while validation == True: # Will loop the question to add another dish if user does not enter y or n
      cont = raw_input("Would you like to add another dish? [y/n] ").lower()
      if cont == "y" or cont == "yes":
        validation = False
      elif cont == "n" or cont == "no":
        print "Thanks for using the menu generator!"
        validation = False
        add = False
      else:
        print "Please enter y(es) or n(o)!"

  except ValueError:
    print "Please enter a number for your price!"


menu_file = open("menu.txt", "w+")
print "Here is your menu for today:"
print
menu_file.write("Today's menu:\n\n")
for item in menu:
  print item + ": €" + menu[item]
  menu_file.write(item + ": €" + menu[item] + "\n")

menu_file.close()