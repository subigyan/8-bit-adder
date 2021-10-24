"""Main module that takes user input and outputs result"""

from logic_gates import * #importing all the names that logic_gates module defines
from bit_and_byte_adder import * #importing all the names that bit_and_byte_adder module defines
from conversions import * #importing all the names that conversion module defines


""""Main function that takes user input calls required function and gives output."""
    
print("----------------------------------------")
print("         Binary Sum Calculator          ")
print("----------------------------------------")
continuation = True
while continuation == True : # Loop occurs if the boolean value for continuation is True 
    print("")
    try: # Trying block of code for errors
            
        decimal_number_1= int(input("Enter first number (Range = 0-255): ")) # Taking decimal value input from user
        if( (decimal_number_1 > 255) or (decimal_number_1 < 0)): # Validating user input
                print ("Invalid value! Please enter a value ranging from 0 to 255.\n")
                continue
            
        decimal_number_2= int(input("Enter second number (Range = 0-255): ")) # Taking decimal value input from user
        if( (decimal_number_2 > 255) or (decimal_number_2 < 0)): # Validating user input
                print ("Invalid value! Please enter a value ranging from 0 to 255.\n")
                continue

        # Converting decimal value input to binary value list
        binary_list_1 = decimal_to_binary_list(decimal_number_1) 
        binary_list_2 = decimal_to_binary_list(decimal_number_2)

        # Converting binary value list binary string
        binary_num_1 = binary_list_to_string(binary_list_1)
        binary_num_2 = binary_list_to_string(binary_list_2)

        print("")
        # Displaying decimal to byte conversion output
        print("The binary value of {} is {}".format(str (decimal_number_1), str (binary_num_1))) 
        print("The binary value of " + str (decimal_number_2) +" is "+ str (binary_num_2) )
        print("")
            
        binary_sum = byte_adder(binary_list_1, binary_list_2) # Calling byte_adder function to calculate sum
        deciaml_sum = decimal_number_1 + decimal_number_2
            
        print("The binary sum value of {} and {} is {}".format(decimal_number_1,decimal_number_2,binary_sum))# Displaying Binary sum
        print("The decimal sum value of {} and {} is {}".format(decimal_number_1,decimal_number_2,deciaml_sum)) # Displaying Decimal sum
        print("")

    except: # Handling error 
        print("Invalid Value!! Please re-enter a valid value\n") # Displaying error message 
        continue 
        
    continue_ = input("Do you wish to continue? (yes/no): ")  # Taking continuation request input from user
        

    if continue_.lower() == "no" : #If user wants to exit the program
        continuation = False;   #breaking the loop by setting continuation boolean value to false
        print("")
        print ("---------Thank You for Using This Program----------")
