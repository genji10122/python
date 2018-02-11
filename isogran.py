
while True:
    word = input("Enter a word: ")

    # red : r  e   d   terminates true
    # book: b   o   o! 0 ==2  false
    # aka:  a  k  a!   a ==2 false

##    
##    #red
##    for num in len(word):
##        #len(word) = 3
##        #num = 1, 2, 3


    letter_list =[] ## creates a new empty list

        
    #red
    #book
    value = "yes" ## create a check value
    for num in range(len(word)-1): ## creates a for loop that goes from 0 to the length of the word minus 1
        #num =  0, 1 ,2
        
        # word[0] = 'r'

        
        letter = word[num] ## assign a variable for each letter
        
        if letter not in letter_list:  ## if the letter is no inside the list it will add it to the list
            letter_list.append(letter)  ## use append to add anything to the list
            
        elif letter in letter_list:  ## if the letter is already in the list it will stop and say OMG and will terminate the search and say false
        
            
            value = "no" ## put check value as no

    ## outside for loop compare value of the check if it's yes print true if it's no print false

    if value == "yes": 
        print("True")
    elif value == "no":
        print("False")
