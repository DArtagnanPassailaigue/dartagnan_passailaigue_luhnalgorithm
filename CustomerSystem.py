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
        # if/else statement that checks if the postal code input is 3 characters or higher
        validatePostalCode(postalcode)
    else:
        print("Invalid postal code.")
        enterCustomerInfo()
    creditcard = input("Enter your credit card number: ")
    if len(creditcard) >= 9:
        # if/else statement that checks if the credit card input is 9 characters or higher
        validateCreditCard(creditcard)
    else:
        print("Invalid credit card number.")
        enterCustomerInfo()
    customerInfo = firstname + "," + lastname + "," + city + "," + postalcode + "," + creditcard
    # variable that stores the input of all the customer information that will go into the temporary file
    folder = os.getcwd()
    fileName = str(folder) + "\\temp.csv"
    with open(fileName, "w") as currentEdit:
        currentEdit.writelines(customerInfo)
    # writes the above statement into a temporary file before going into the user's selected file
    
def validatePostalCode(code):
    '''Uses the database of postal codes in postal_codes.csv to cross reference the postal code input by the user'''
    folder = os.getcwd()
    fileName = str(folder) + "\\postal_codes.csv"
    with open(fileName, "r") as readFile:
        postalCodeFile = csv.reader(readFile, delimiter='|')
        # reads the postal code file and states the delimiter
        for row in postalCodeFile:
            codeInFile = row[0].strip().upper()[:3]
            # strips the row in question in the postal code file of everything except the first three postal code digits and ensures that they are capitalized
            if code.strip().upper()[:3] == codeInFile:
                print("Postal code approved!")
                return
                # takes the postal code input and strips it to the first three digits and ensures that it is capitalized
                # if the input matches the line currently being checked, the postal code is approved and the function is returned
        print("Postal code was not found :(")
        enterCustomerInfo()
        # if no postal code match is found, the program informs the user and begins the "enter customer info" function again

def validateCreditCard(number):
    '''Uses the Luhn Algorithm to validate the credit card input by the user'''
    checkSum = 0
    # defines the local checkSum variable
    oddOrEven = len(number) % 2
    # defines the odd_or_even variable and establishes it as the length of the credit card number input by a factor of two
    for i in range(len(number) -1, -1, -1):
        # creates a for loop for the length of the user input that reverses the order of the numbers input and goes through them one by one
        x = int(number[i])
        if (i + 1) % 2 != oddOrEven:
            x = x * 2
            # determines if the number being checked is even or odd, and doubles it if it is even
        if x > 9:
            x = x - 9
            # if the sum is greater than 9, subtract it by 9, which has the same effect as if the two digits in the tens and ones positions were added
        checkSum = checkSum + x
        # sums the two multiplied digits
    result = checkSum % 10 == 0
    # checks if the sum can be factored by ten to equal zero and saves the true or false response to teh variable "result"
    if result == True:
        print("Credit card validated!")
        return
        # validates the credit card and returns the function if the result variable is true
    else:
        print("Credit card declined :(")
        enterCustomerInfo()
    
def generateCustomerDataFile():
    '''Generates a data file for the customer currently in the temp.csv file'''
    folderChoice = input("Enter the name of the folder you wish to save to: ")
    folder = os.getcwd()
    fileName = str(folder) + "\\temp.csv"
    with open(fileName, "r") as currentEdit_r:
        tempContents = currentEdit_r.read()
    # reads the contents of the temp file and saves it to the variable tempContents
    fileName = str(folder) + "\\userID.txt"
    with open(fileName, "r") as currentEdit_r:
        userID = currentEdit_r.read()
    # reads the contents of the userid.txt file to determine the customer's unique ID and saves it to the userID variable
    userID = int(userID)
    # changes the numerical userID from a string to an integer
    fileName = str(folder) + "\\" + folderChoice
    with open(fileName, "a") as currentEdit_a:
        currentEdit_a.write(str(userID) + "," + tempContents + "\n")
    # appends the contents of userID and tempcontents to the user's chosen file
    fileName = str(folder) + "\\userID.txt"
    with open(fileName, "w") as currentEdit_w:
        userID += 1
        currentEdit_w.write(str(userID))
    # increases userID by one and prints the new userID value to the userID.txt file

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