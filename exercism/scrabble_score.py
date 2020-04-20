"""
Introduction
Given a word, compute the scrabble score for that word.

Letter Values
You'll need these:

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10

Examples
"cabbage" should be scored as worth 14 points:
"total" should be scored as worht 5 points:

3 points for C
1 point for A, twice
3 points for B, twice
2 points for G
1 point for E

And to total:

3 + 2*1 + 2*3 + 2 + 1
= 3 + 2 + 6 + 3
= 5 + 9
= 14

Extensions
You can play a double or a triple letter.
You can play a double or a triple word.

"""

# write a function that takes in a word 
def score_scrabble(str):
    #during testing, an edge case came up
    #our letter values are in CAPS, and the user might 
    #input a string that is lowercased, so force the string to be captilzed 

    #use the given Letter Values and define them here 
    # (optional: list, dictionary, mutliple values)

    letters = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G':2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3, 
        'F': 4, 'H': 4, 'V': 4, 'W': 4,'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10         
    }

    #define sum to keep track of the total 
    sum = 0 

    #Loop through the str and for every character in the string 
    #check the letter dictionary and get the value 
    for char in str:
        #convert char to captial letter 
        char = char.capitalize()
        #now add the letter's value to sum 
        sum += letters[char]
    
    #now return the total sum 
    return sum



if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    """
    Test Cases:

        Good/Normal Input:
            "CABBAGE" should be scored as worth 14 points
            "TOTAL" should be scored as worht 5 points
        
        Bad/Unusual Input:
            - if the user enters number 
        
        Edge Cases Input:
            our letter are captiziled, so what if the user enters a lowercase letter 
        
    """


    
    print("Total Sum for", args[0], ":", score_scrabble(args[0]))
