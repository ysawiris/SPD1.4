'''
    Problem:
        Find the 5th largest element in an unsorted array. 
        Note that it is the kth largest element in the sorted order, not the kth distinct element.
    
    Example 1:
        Input: [3,2,1,5,6,4] 
        Output: No 5th Largest Number
    
    Example 2:
        Input: [3,2,3,1,2,4,5,5,6] 
        Output: 4
    Note:
        You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

import math

def find5thLargest(arr):

    #Create Variables to keep track of top 5 largest numbers
    #Remember we only want the 5th largest one 
    num_1st = -math.inf
    num_2nd = -math.inf
    num_3rd = -math.inf
    num_4th = -math.inf
    num_5th = -math.inf




    for index, number in enumerate(arr):
        print("index: ", (index , number))
        
        #check if the num is greater than 1st Largest Number
        #else set it as the 2nd largest 
        if number > num_1st:
            num_2nd = num_1st
            num_1st = number
            #Variable Table
            print("Largest ", num_1st, num_2nd, num_3rd, num_4th, num_5th)
            

        elif number > num_2nd:
            num_5th = num_4th
            num_4th = num_3rd
            num_3rd = num_2nd
            num_2nd = number
            #Variable Table
            print("Largest ", num_1st, num_2nd, num_3rd, num_4th, num_5th)
            
            
        elif number > num_3rd:
            num_5th = num_4th
            num_4th = num_3rd
            num_3rd = number
            #Variable Table
            print("Largest ", num_1st, num_2nd, num_3rd, num_4th, num_5th)
            
    
        elif number > num_4th:
            num_5th = num_4th
            num_4th = number
            #Variable Table
            print("Largest ", num_1st, num_2nd, num_3rd, num_4th, num_5th)
            

        elif number > num_5th:
            num_5th = number
            #Variable Table
            print("Largest ", num_1st, num_2nd, num_3rd, num_4th, num_5th)
            continue
        
    if num_5th == -math.inf:
        return "There is no 5th largest number"

    return ("Num 5th ", num_5th)



if __name__ == "__main__":
    

    arr = [3,2,3,1,2,4,5,5,6,7] 
    print(find5thLargest(arr))
    
