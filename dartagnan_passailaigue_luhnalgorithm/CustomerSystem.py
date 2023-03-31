import os
import csv

def printMenu():
    '''The menu that allows users to choose an action in the program'''
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

def enterCustomerInfo():
    '''Allows the user to input the customer's information, and validates the postal code and credit card inputs'''
    firstname = input("Enter your first name: ")
    lastname = input("Enter your surname: ")
    city = input("Enter the name of your city: ")
    postalcode = input("Enter your postal code: ")
    if len(postalcode) >= 3:
        validatePostalCode(postalcode)
    else:
        print("Invalid postal code.")
        enterCustomerInfo()
    creditcard = input("Enter your credit card number (i will not steal your money i promise): ")
    if len(creditcard) >= 9:
        validateCreditCard(creditcard)
    else:
        print("Invalid credit card number.")
        enterCustomerInfo()
    customerInfo = firstname + "," + lastname + "," + city + "," + postalcode + "," + creditcard
    folder = os.getcwd()
    fileName = str(folder) + "/temp.csv"
    with open(fileName, "w") as currentEdit:
        currentEdit.writelines(customerInfo)
    
def validatePostalCode(code):
    '''Uses the database of postal codes in postal_codes.csv to cross reference the postal code input by the user'''
    folder = os.getcwd()
    fileName = str(folder) + "/dartagnan_passailaigue_luhnalgorithm/postal_codes.csv"
    with open(fileName, "r") as readFile:
        postalCodeFile = csv.reader(readFile, delimiter='|')
        for row in postalCodeFile:
            codesInFile = row[0].strip().upper()[:3]
            if code.strip()[:3] == codesInFile:
                print("Postal code approved!")
                return
        print("Postal code was not found :(")
        enterCustomerInfo()

def validateCreditCard(number):
    '''Uses the Luhn Algorithm to validate the credit card input by the user'''
    checkSum = 0
    odd_or_even = len(number) % 2
    for i in range(len(number) -1, -1, -1):
        x = int(number[i])
        if (i + 1) % 2 != odd_or_even:
            x = x * 2
        if x > 9:
            x = x - 9
        checkSum = checkSum + x
    result = checkSum % 10 == 0
    if result == True:
        print("Credit card validated!")
    else:
        print("Credit card declined :(")
        enterCustomerInfo()
    
def generateCustomerDataFile():
    '''Generates a data file for the customer currently in the temp.csv file'''
    folderChoice = input("Enter the name of the folder you wish to save to: ")
    folder = os.getcwd()
    fileName = str(folder) + "/temp.csv"
    with open(fileName, "r") as currentEdit_r:
        tempContents = currentEdit_r.read()
    fileName = str(folder) + "/userID.txt"
    with open(fileName, "r") as currentEdit_r:
        userID = currentEdit_r.read()
    userID = int(userID)
    fileName = str(folder) + "/" + folderChoice
    with open(fileName, "a") as currentEdit_a:
        currentEdit_a.write(str(userID) + "," + tempContents + "\n")
    fileName = str(folder) + "/userID.txt"
    with open(fileName, "w") as currentEdit_w:
        userID += 1
        currentEdit_w.write(str(userID))

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################

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
userID = 0

while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input()      # User selection from the menu

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