def del_o():
    ''' it for loops through the word and immediatley deletes all the o's or O's
    poop
    >>>pp
    '''
    word = input("Enter a word: ")

    ## all the letters that are vowels should be deleted

    # Hint: for loop through the word and delete the letters
    # at the index of the vowel

    
    new_word = ""
    
    for num in range(len(word)):
        letter = word[num]
        if letter not in ["o", "O"]:
            new_word = new_word + letter
    print(new_word)
    return new_word

while input != '':   
    del_o()
