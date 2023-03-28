import os

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

'''
    These functions are to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''

def enterCustomerInfo():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your surname: ")
    city = input("Enter the name of your city: ")
    postalcode = input("Enter your postal code: ")
    validatePostalCode(postalcode)
    creditcard = input("Enter your credit card number (i will not steal your money i promise): ")
    validateCreditCard(creditcard)
    customerInfo = str(firstname + "," + lastname + "," + city + "," + postalcode + "," + creditcard)
    enterInformation(customerInfo, "\\dartagnan_passailaigue_luhnalgorithm\\temp.txt")
    
def validatePostalCode(code):
    pass    # Remove this pass statement and add your own code below

def validateCreditCard(number):
    pass    # Remove this pass statement and add your own code below

def generateCustomerDataFile():
    folderChoice = input("Enter the filename you wish to save to: ")

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################

def enterInformation(text, file):
    folder = os.getcwd()
    fileName = str(folder) + file
    currentEdit = open(fileName, "w")
    currentEdit.writelines(text)
    currentEdit.close

####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")