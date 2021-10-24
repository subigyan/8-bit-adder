"""Module Consisting Bit adder and Byte adder function"""

from logic_gates import * #importing all the names that logic_gates module defines
from conversions import * #importing all the names that conversion module defines

def bit_adder(upper_bit,lower_bit,carry_in):
    """Calculates the carry out and sum bit using upper, lower and carryin bit and is based upon the bit adder model."""
    
    x = upper_bit
    y = lower_bit
    # Using logic gates function based on the bit adder digit circut model
    x_XOR_y = XOR(x,y)

    # Finding the carry in bit value 
    x_AND_y = AND(x,y)
    x_XOR_y_AND_carry_in= AND(x_XOR_y,carry_in)
    carry_out = NOT(NOR(x_AND_y,x_XOR_y_AND_carry_in))

    # Finding the carry in sum value 
    x_XOR_y_NAND_carry_in= NAND(x_XOR_y, carry_in )
    x_XOR_y_OR_carry_in = OR(x_XOR_y, carry_in)
    bit_sum= AND(x_XOR_y_NAND_carry_in, x_XOR_y_OR_carry_in)
    
    return (carry_out,bit_sum) # Returning carry out and sum bit as a tuple

def byte_adder(binary_num_list_1 ,binary_num_list_2):
    """Based on the bit adder function takes two byte of binary value as input and returns a their sum in string."""
    
    carry_in = 0
    sum_ = []
    for i in range (7,-1,-1): # For loop that loops eight times for eight bit adder calculation . 
        x = binary_num_list_1[i]
        y = binary_num_list_2[i]
        carry_out,bit_sum = bit_adder(x,y,carry_in) # Calling bit_adder function find the carry out bit and sum bit
        sum_.append(bit_sum)
        carry_in = carry_out
    if carry_out == 1:
        sum_. append(carry_out)
    binary_sum_list = sum_[::-1] # Reversing the string using list operator
    binary_sum = binary_list_to_string(binary_sum_list) # Calling binary_list_to_string function to convert binary list to string
    
    return binary_sum # Returning a string of binary sum 

