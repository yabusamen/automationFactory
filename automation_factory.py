'''
    An automated package sorter. 
    
    #TODO Create a detailed description of the class.
'''
class AutomationFactory: 

    # If a package has a volume of 1 million (cm³) then it is categorized as 'BULKY'
    BULKY_PACKAGE_VOLUME = 1000000 
    # If any of the package dimmensions are greater than or equal to 150cm, then it is categorized as 'BULKY'
    BULKY_PACKAGE_DIMMENSION = 150

    # If a package has a weight of 20 (kg) then it is categorized as 'HEAVY'
    MASSIVE_WEIGHT = 20

    # Define the constants to represent the different STACKS
    STANDARD = "STANDARD"
    SPECIAL = 'SPECIAL'
    REJECTED = 'REJECTED'

    # A simple error message, in the event of exceptions
    ERROR_RESPONSE = "N/A. Something went wrong"

    '''
    This method takes in a package's dimmensions and weight - and returns the correct 'Stack' that it should categorized in. (standard, special, or rejected)
    '''
    def sort(self, width, height, length, mass): 

        # Validate the input variables. They should all be numeric. Also non-negative
        try: 
            width_value = float(width)
            height_value = float(height)
            length_value = float(length)
            mass_value = float(mass)
            if self.isAnyValuesNegativeOrZero(width, height, length, mass): 
                raise Exception
        except:
            # For the sake of this program, just print a message to the console and exit. (Ideally we would throw exception and the caller would handle it)
            print("Sorry there was a problem with your entry. Please be sure to enter numeric values greater than zero!")
            return self.ERROR_RESPONSE
        
        # find out if the package is too bulky (compute its volume)
        volume = length_value * width_value * height_value 
        isVolumeBulky = volume >= self.BULKY_PACKAGE_VOLUME

        # check if one of the dimmensions is too long (greater or equal to 150 cm)
        isDimmensionTooLong = (width_value >= self.BULKY_PACKAGE_DIMMENSION or 
                               height_value >= self.BULKY_PACKAGE_DIMMENSION or 
                               length_value >= self.BULKY_PACKAGE_DIMMENSION)


        isPackageBulky = isVolumeBulky or isDimmensionTooLong

        # check if the package weight is considered 'HEAVY'
        isPackageMassive = mass_value >= self.MASSIVE_WEIGHT

        if isPackageBulky and isPackageMassive: 
            # REJECT this package if it is bulky AND heavy
            return self.REJECTED
        elif isPackageBulky or isPackageMassive: 
            # SPECIAL package if it is either bulky OR heavy
            return self.SPECIAL
        else: 
            # STANDARD packages are neither bulky nor heavy
            return self.STANDARD
        
    '''
    A method to help with input validation. The values should all be greater than zero.
    '''
    def isAnyValuesNegativeOrZero(self, width, height, length, mass): 
        return (width <= 0.0 or 
                height <= 0.0 or 
                length <= 0.0 or 
                mass <= 0.0)

    def __init__(self):
        pass



def main(): 
    # Initialize an instance of the automation factory class.
    automationFactory = AutomationFactory()

    # Allow the user of this program to either (1) Interact with the program by entering the dimmensions of a package. Or (2) run some default test cases
    selection = input('Enter \'Y\' if you would like to enter Interactive Mode (enter package dimmensions yourself).\nOtherwise, enter \'N\' to run some default test cases for our package sorting program.\n')
    selection = selection.lower()
    if selection == "y":
        while True: 
            width = input("Please enter the width (cm): ")
            height = input("Please enter the height (cm): ")
            length = input("Please enter the length (cm): ")
            mass = input("Please enter the mass (kg): ") 

            # Input validation - Make sure user entered a numerical value
            width_value = None
            height_value = None
            length_value = None
            mass_value = None
            try: 
                width_value = float(width)
                height_value = float(height)
                length_value = float(length)
                mass_value = float(mass)
            except:
                # Ideally we would handle exception properly here, but leaving it empty for simplicity.
                return

            print("This package is categorized as: " + automationFactory.sort(width_value, height_value, length_value, mass_value))
    elif selection == 'n': 
        ''' DEFAULT TEST CASES BELOW '''

        # Expected: STANDARD
        print("TEST_1 (10, 15, 20, 7)\nExpected: STANDARD.\tActual: " + automationFactory.sort(10, 15, 20, 7), end="\n\n")
        # Expected: SPECIAL (This one should be bulky b/c of the 160 dimmension)
        print("TEST_2 (160, 15, 20, 16)\nExpected: SPECIAL.\tActual: " + automationFactory.sort(160, 15, 20, 16), end="\n\n")
        # Expected: SPECIAL (This one should be bulky b/c of overall volume)
        print("TEST_3 (1000, 100, 20, 13)\nExpected: SPECIAL.\tActual: " + automationFactory.sort(1000, 100, 20, 13), end="\n\n")
        # Expected: REJECTED 
        print("TEST_4 (1000, 100, 20, 100)\nExpected: REJECTED.\tActual: " + automationFactory.sort(1000, 100, 20, 100), end="\n\n")
        # Expected: Error message (invalid input. Non-numeric value) 
        print("TEST_5 (\"abc\", 100, 20, 100)\nExpected: some error message.\tActual: " + automationFactory.sort("abc", 100, 20, 100), end="\n\n")
        # Expected: Error message (invalid input. Negative number) 
        print("TEST_6 (-1, 100, 20, 100)\nExpected: some error message.\tActual: " + automationFactory.sort(-1, 100, 20, 100), end="\n\n")
        # Expected: Error message (invalid input. zero float value) 
        print("TEST_7 (0.0, 100, 50, 12)\nExpected: some error message.\tActual: " + automationFactory.sort(0.0, 100, 50, 12), end="\n\n")
        # Expected: Error message (invalid input. Malformatted zero value) 
        print("TEST_8 (00, 15, 35.7, 19.9999)\nExpected: STANDARD.\tActual: " + automationFactory.sort(00, 15, 35.7, 19.9999), end="\n\n")
        # Expected: STANDARD
        print("TEST_9 (3.0, 15, 35.7, 19.9999)\nExpected: STANDARD.\tActual: " + automationFactory.sort(3.0, 15, 35.7, 19.9999), end="\n\n")
        # Expected: SPECIAL (This one should be heavy)
        print("TEST_10 (8.0, 18, 16, 190)\nExpected: SPECIAL.\tActual: " + automationFactory.sort(8.0, 18, 16, 190), end="\n\n")
        # Expected: STANDARD (This one should be heavy)
        print("TEST_11 (0.00001, 0.0003, 0.5, 0.3)\nExpected: STANDARD.\tActual: " + automationFactory.sort(0.00001, 0.0003, 0.5, 0.3), end="\n\n")
    else: 
        print("Your selection was not one of the options. Please try again (enter Y or N)")

if __name__=="__main__": 
    main()