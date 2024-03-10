def is_binary_number(num):                               #Check if the input is binary 
    return all(bit in '01' for bit in num)

def twos_complement(binary_num):                         #twos complement function 
    twos_comp = ""
    carried_num = 1                 
#similar to the addition function as we just add one to the ones complement
    for digit in reversed(ones_complement(binary_num)):  #We reverse the number as we add to the rightmost digit
        sum_of_each = int(digit) + carried_num           #calculate the sum of each digit and the carry
        twos_comp = str(sum_of_each % 2) + twos_comp     #the modulus of the sum is the digit of the twos complement
        carried_num = sum_of_each // 2                   #Updates the carried number
    return twos_comp

def ones_complement(binary_num):                         #ones complement function
    ones_comp = ''
    for digit in binary_num:                           
        ones_comp += '0' if digit == '1' else '1'      #substitutes each one with zero and vise verca
    return ones_comp

def binary_addition(num1, num2):                        # addition function
    max_len = max(len(num1), len(num2))                 # Calculates the maximum of the length of the two inputs
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
#the previous 2 steps make sure that the two inputs have the same length by filling the remaining digits with zeros
    carried_num = 0
    result = ''
    for i in range(max_len - 1, -1, -1):                           #Reversing the numbers to add to the rightmost digit
        sum_of_each = int(num1[i]) + int(num2[i]) + carried_num    #calculate the sum of each digit and the carry
        result = str(sum_of_each % 2) + result                     #the modulus of the sum is the digit of the result
        carried_num = sum_of_each // 2                             #Updates the carried number
    if carried_num:
        result = '1' + result                           #adds an additional 1 to the result in case of a remaining carry
    return result

def binary_subtraction(num1, num2):                     #Subtraction function
    num2_comp = twos_complement(num2)                   #calculates the twos complement of one of the numbers
    result = binary_addition(num1, num2_comp)           #Subtraction of two numbers= the addition of one number and the twos complement of the other
    if len(result) > len(num1):                         #Indicates if there was a carry at the end
        result = result[1:]                             #Ignore the carry by ignoring the digit with index[0]
    return result

while True:                                                     #a loop until the input meets the condition
    print("** binary calculator **")
    print("A) Insert new numbers")
    print("B) Exit")

    choice_menu1 = input("Enter your choice (A/B): ").upper()   #to make the input uppercase if lowercase to meet the condition

    if choice_menu1 == 'A':
        while True:                                             #a loop until the input meets the condition 
            binary_num1 = input("Enter the first binary number: ")
            if is_binary_number(binary_num1):
                break
            else:
                print("Please insert a valid binary number.\n")

        while True:  
            print("** please select the operation **")
            print("A) Compute one's complement")
            print("B) Compute two's complement")
            print("C) Addition")
            print("D) Subtraction")                                         #a loop until the input meets the condition
            choice_menu2 = input("Enter your choice (A/B/C/D): ").upper()
            if choice_menu2 in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Please select a valid choice.\n")

        if choice_menu2 in ['A', 'B']:
            if choice_menu2 == 'A':
                result = ones_complement(binary_num1)
                print(f"One's complement result: {result}")
            elif choice_menu2 == 'B':
                result = twos_complement(binary_num1)
                print(f"Two's complement result: {result}")
        elif choice_menu2 in ['C', 'D']:
            while True:                                           #a loop until the input meets the condition
                binary_num2 = input("Enter the second binary number: ")
                if is_binary_number(binary_num2):
                    break
                else:
                    print("Please insert a valid binary number.\n")

            if choice_menu2 == 'C':
                result = binary_addition(binary_num1, binary_num2)
                print(f"Addition result: {result}")
            elif choice_menu2 == 'D':
                result = binary_subtraction(binary_num1, binary_num2)
                print(f"Subtraction result: {result}")
        else:
            print("Please select a valid choice.\n")
        print("Returning to Menu 1...")
    elif choice_menu1 == 'B':
        print("Exiting the program.")
        print('Thanks for using our program!')
        break
    else:
        print("Please select a valid choice.\n")

#Mario Saber Shawqy      20230305
