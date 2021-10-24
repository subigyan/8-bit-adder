"""Module consisting of functions created for conversions"""

def binary_list_to_string(list_):
    """Converts a list of binary numbers into a string of binary number negating the usless 0 bits infornt."""
    
    string = ""
    for items in list_: # Iterating items through the input list
        if items == 1:
            highest_bit_index = list_.index(items)
            for i in range (highest_bit_index, len(list_)):  # Iterating items through the input list withing a certain range
                string = string + str(list_[i]) # Conctinating list items to binary string
            if(string==""):
                return 0
            else:
                return string
            
def decimal_to_binary_list(number):
    """Converts a decimal number to a byte sized binary numbers in a list."""
    
    byte_list=[0,0,0,0,0,0,0,0] # Initializing empty byte list
    count=0
    while number>=1 and count<8: # Looping eight times and until number is less than 1
        if number%2==0:
            byte_list[count]=0
        else:
            byte_list[count]=1
        number=number//2
        count+=1
    binary_list=byte_list[::-1] # reversing the list using list operation
    return binary_list #returning byte sized binary number in a list 

