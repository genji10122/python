def pothole_to_camel(hole):
    '''(str) --> (str)
    return a camel case version of the string pothole
    >>> pothole_to_camel ('comp_sci')
    'compSci'
    '''


    # WORD THAT WE ARE CONSIDERING IS CALLED POTHOLE
    #we look at every letter in pothole
    # if we see an underscore, we delete that letter
    # the next letter after underscore is turned into a capital letter
    # in camel there is a cap in only one word (2nd word) and no spaces or underscores
    # in pothole there are underscores but no caps or spaces

    # store index of underscores in a list
    # delete the letters at that index; make the next index a capital letter


underscore_list =[]    


for num in range(len(word)-1):

    
      letter = word[num]
      

       if letter == "_" :
            underscore_list.append(num)
