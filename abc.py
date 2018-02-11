def order(s):
    ''' (string) -> (string)
    it takes in a string s and orders the words
    >>> order( "GENGU IS THE BEST")
    "BEST GENGU IS THE"

    >>> order("This is a sentence")
    "a is sentence This"
    '''
    w = s.split() ## splits all the words from the sentence in a list
    w.sort(reverse = True) ## sorts the words in the list from first letter
    
    empty = ""
    for genji in w:
        empty = genji + " " + empty ##it adds all the indiviual words and turns it into one big string
    return empty



def organize(n):
    ''' (int) -> (int)
    it takes in integers and organizes the numbers from least to greatest
    >>> organize (4321)
    1234
    '''
    s =  str(n)
    m = s.split()
    m.sort(reverse = True)

    empty = ""
    for menji in m:
        empty = menji + " " + empty
    num = int(empty)

    
    
    return num



    order ()
    organize ()
