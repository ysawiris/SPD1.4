"""
Word Count 

Introduction
Given a phrase, count the occurrences of each word in that phrase.

For the purposes of this exercise you can expect that a word will always be one of:
    A number composed of one or more ASCII digits (ie "0" or "1234") OR
    A simple word composed of one or more ASCII letters (ie "a" or "they") OR
    A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")

When counting words you can assume the following rules:
    The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
    The count is unordered; the tests will ignore how words and counts are ordered
    Other than the apostrophe in a contraction all forms of punctuation are ignored
    The words can be separated by any form of whitespace (ie "\t", "\n", " ")

For example, for the phrase "That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled. the count would be:

    that's: 1
    the: 2
    password: 2
    123: 1
    cried: 1
    special: 1
    agent: 1
    so: 1
    i: 1
    fled: 1
"""
#write a function that will strip our word
def stripWordPunctuation(word):
    return word.strip("#^%$@&.,()<>\"\\'~?!;*:[]-+/&—\n` ")

#write a function that takes in a list of words 
def word_count(words):
    #define a dictionary that will keep track of our words and count 
    count = {}
    #loop through each word in words 
    for word in words:
        #strip that word 
        word = stripWordPunctuation(word)

        #check if we have seen the word before 
        #by seeing if its in our count dictionary 
        if word in count.keys():
            #we have seen this word before 
            #so lets add one to its count 
            count[word] += 1
        else:
            #this is our 1st time seeing this word
            #lets set its value equal to 1 
            count[word] = 1 
    
    return count

if __name__ == "__main__":
    # import sys
    # args = sys.argv[1:]

    # print("word count :", word_count(args))

    test = ['money %&@&(', 'money \n']
    
    print("word count :", word_count(test))