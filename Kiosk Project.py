#Getting files

import os

#Function that prints the menu choices
def PrintMenu():
    print('Option 1: Pizza Without Toppings $7.99')
    
    print('Option 2: Pizza With Toppings $11.99')
    
    print('Option 3: Spaghetti and Meatballs $15.99')
    
    print('Option 4: Classic Italian Submarine Sandwich $8.99')
    
    print('Option 5: Lasagna and Garlic Knots $19.99')

    print('\n')

#Function to find price
def GetTotalPrice(priceOfChoice, finalTotal, count):
  if count == 1:
      taxRate = 0.08125
      totalTaxAmount = priceOfChoice * taxRate

      priceWithTax = totalTaxAmount + priceOfChoice
      
      return(priceWithTax)
  else:
      taxRate = 0.08125
      totalTaxAmount = priceOfChoice * taxRate

      priceWithTax = totalTaxAmount + priceOfChoice

      totalPrice = finalTotal + priceWithTax
      
      return(totalPrice)

#Setting up choice variables
choiceOnePrice = 7.99
choiceTwoPrice = 11.99
choiceThreePrice = 15.99
choiceFourPrice = 8.99
choiceFivePrice = 19.99

#Print the menu
PrintMenu()

#Input from user
print('Please input a number between 1 and 5 to pick one of the items in the kiosk')
print('If you need to see the menu again, enter 0')
print('Enter -1 to quit')

userChoice = int(input())

finalTotal = 0

count = 0

#While the entered input is not one, perform the code below
while userChoice != -1:

    #Add one to the counter variable
    count = count + 1
    
    #If statements to differentiate totals
    if userChoice == 1:
      priceOfChoice = choiceOnePrice
      
      priceWithTax = GetTotalPrice(priceOfChoice, finalTotal, count)
      
      finalTotal = priceWithTax
      
      print('\n')
      
      print('Your Final Price is:', '$' + format(finalTotal, ',.2f'))
      print('\n')
      
      print('Please input a number between 1 and 5 to pick another item in the kiosk')
      print('If you need to see the menu again, enter 0')
      print('Enter -1 to quit')

      userChoice = int(input())
      
    elif userChoice == 2:
      priceOfChoice = choiceTwoPrice
      
      priceWithTax = GetTotalPrice(priceOfChoice, finalTotal, count)
      
      finalTotal = priceWithTax
      
      print('\n')
      
      print('Your Final Price is:', '$' + format(finalTotal, ',.2f'))
      print('\n')

      print('Please input a number between 1 and 5 to pick another item in the kiosk')
      print('If you need to see the menu again, enter 0')
      print('Enter -1 to quit')

      userChoice = int(input())
      
    elif userChoice == 3:
      priceOfChoice = choiceThreePrice
      
      priceWithTax = GetTotalPrice(priceOfChoice, finalTotal, count)
      
      finalTotal = priceWithTax
      
      print('\n')
      
      print('Your Final Price is:', '$' + format(finalTotal, ',.2f'))
      print('\n')

      print('Please input a number between 1 and 5 to pick another item in the kiosk')
      print('If you need to see the menu again, enter 0')
      print('Enter -1 to quit')

      userChoice = int(input())
      
    elif userChoice == 4:
      priceOfChoice = choiceFourPrice
      
      priceWithTax = GetTotalPrice(priceOfChoice, finalTotal, count)
      
      finalTotal = priceWithTax
      
      print('\n')
      
      print('Your Final Price is:', '$' + format(finalTotal, ',.2f'))
      print('\n')

      print('Please input a number between 1 and 5 to pick another item in the kiosk')
      print('If you need to see the menu again, enter 0')
      print('Enter -1 to quit')

      userChoice = int(input())
      
    elif userChoice == 5:
      priceOfChoice = choiceFivePrice
      
      priceWithTax = GetTotalPrice(priceOfChoice, finalTotal, count)
      
      finalTotal = priceWithTax
      
      print('\n')
      
      print('Your Final Price is:', '$' + format(finalTotal, ',.2f'))
      print('\n')

      print('Please input a number between 1 and 5 to pick another item in the kiosk')
      print('If you need to see the menu again, enter 0')
      print('Enter -1 to quit')

      userChoice = int(input())

    elif userChoice == 0:
      print('\n')

      PrintMenu()

      print('Please input a number between 1 and 5 to pick another item in the kiosk')
      print('If you need to see the menu again, enter 0')
      print('Enter -1 to quit')

      userChoice = int(input())
      
    else:
      print('\n')
      print('Error: Invalid Selection')
      print('\n')

      print('Please input a number between 1 and 5 to pick another item in the kiosk')
      print('If you need to see the menu again, enter 0')
      print('Enter -1 to quit')

      userChoice = int(input())


print('\n')
print('Have a nice day!')
os.system("PAUSE")
