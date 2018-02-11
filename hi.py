


def hi (o):
    ''' (int) -> (boolean) 
    it takes in an integer o and tells us if it is true positive or false negative
    >>> hi(-1)
    "THIS IS A NEGATIVE NUMERO BRO"
    >>> hi(7)
    "S'ALL POSITIVE BRO"
    >>> hi(0)
    "THIS NUMERO AINT NEGATIVE NOR POSITIVE BRO"
    '''
    if o < 0:
        return "THIS IS A NEGATIVE NUMERO BRO"
    if o > 0:
        return "S'ALL POSITIVE BRO"
    if o == 0:
        return "THIS NUMERO AINT NEGATIVE NOR POSITIVE BRO"



def meme (v):
    ''' (int) -> (boolean)
    it takes in an integer v and tells us if it is odd or even
    >>> meme(7)
    "THIS IS RATHER ODD"
    >>> meme(44)
    "THIS IS ODDLY EVEN"
    '''
    if v%2 == 1:
        return "THIS IS RATHER ODD"
    if v%2 == 0:
        return "THIS IS ODDLY EVEN"

        
hi()
meme()

    

    
