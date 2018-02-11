from random import randint

name = ['Genji', 'Widowmaker' , 'Junkrat']
verb = ['kicks' , 'destroyes' , 'bombs']
noun = ['Hanzo' , 'gerrard' , 'people']

def sentences(words):
    ''' (list of strings) -> (string)
    returns any word from a list of words
    >>> sentences(['Genji', 'Widowmaker' , 'Junkrat'])
    >>> Widowmaker
    '''

    ## ['Genji', 'Widowmaker' , 'Junkrat']
    ##    0         1             2
    ##  LENGTH = 3 
    
    numwords = len(words) - 1 ##length of 3, acces last element which is 2
    pick = randint(0, numwords)
    return words[pick]
    
   
print(sentences(name) , sentences(verb) , sentences (noun) , end= '.\n')   
