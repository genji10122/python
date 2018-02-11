def replace_vowels():
    ''' it for loops through the word and immediatley deletes all vowels like a, e, i, o, u:
    apple
    >>>ppl
    '''
    word = input("Enter a word: ")

    ## all the letters that are vowels should be deleted

    # Hint: for loop through the word and delete the letters
    # at the index of the vowel

    
    new_word = ""
    
    for num in range(len(word)):
        letter = word[num]
        if letter not in ["a", "e", "i", "o", "u"]:
            new_word = new_word + letter
        else:
             new_word = new_word + 0
    print(new_word)
    return new_word

def kill_six():
    
    '''it for loops through the number and immediatley kills any six it finds
    201667
    >>>2017
    '''
    num = input("Enter a number")
    
    new_number = ""

    for index in range(len(num)):
       single_num = num[index]
       if single_num != "6":
           new_number = new_number + single_num
    print(new_number)
    return new_number


def kill_six_num():
    
    '''it for loops through the number and immediatley kills any six it finds
    201667
    >>>2017
    '''
    string_num = input("Enter a number")
    num = int(string_num)
    
    new_number = 0

    for index in range(len(num)):
       single_num = num[index]
       if single_num != "6":
           new_number = new_number + single_num
    print(new_number)
    return new_number

while True:
    kill_six()
