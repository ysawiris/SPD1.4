"""
Problem: Find the longest substring of unique letters in a given string of n letters.


Input: string : ex. "Mississippi"
                    "Homework"

Output: "M"
        "mew"



"""



str = "Homework"

"Loop over the string and check the char and if we saw it before"
"if not then we can assume that its a unique value"
"then we need to keep going and see how long the substring remains unique "
"return the longest substring"


def substring(str):
    # use this to keep track of longest subtring 
    dict = {}

    for char in str:
        substr = ""
        #if not in dict.key(), lets the char to dict
        #if it is, we need to save the substr and delete the common char 
        if char in dict.keys():
            
        else: 
            dict[char] = 1 
            substr = substr + char 



