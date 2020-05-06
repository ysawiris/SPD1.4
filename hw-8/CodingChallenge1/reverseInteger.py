"""
Problem:
    Given a 32-bit signed integer, reverse digits of an integer.

Test Case 1:
    Input: 123
    Output: 321
Test Case 2:
    Input: -123
    Output: -321
Test Case 3:
    Input: 120
    Output: 21
"""
from stack import LinkedStack

def reverse(nums):
    #declare your stack
    Stack = LinkedStack() #init the stack 
        
    #declare a variable to get track of the reversed number 
    reversed = []

    #add each number in nums to the stack 
    for num in nums: # Loop through the whole list O(n)
        if num == '-':
            reversed.append(num) #adds sign to list O(1)
        if num.isdigit():
            Stack.push(num) #adds num to stack O(1)

    #traverse through the stack 
    while Stack.length() > 0: # Loops through the whole stack 
        #add the head of the stack then delete the head 
        reversed.append(Stack.peek()) # adds number back to list O(1)
        Stack.pop() # deletes current stack to move to the next one O(1)


    if reversed[0] == '-':
        if reversed[1] == '0':
            reversed.pop(1) #removes a digit O(1)
    
    if reversed[0] == '0':
        reversed.pop(0) #removes a digit O(1)
    
    return "".join(reversed)


print("Test Case: '123' reversed: ",reverse('123'))
print("Test Case: '-123' reversed: ",reverse('-123'))
print("Test Case: '1230' reversed: ",reverse('1230'))