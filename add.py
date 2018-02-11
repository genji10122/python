def addition(x, y):
	'''(int, int) -> (int)
	the function takes in two integers x and y and returns their sum
	
	>>> addition(9, 10)
	19

	>>> additon(10, 11)
	21
	'''
	return x + y 
def subtraction (a, b):
	'''(int, int) -> (int)
	the function takes in 2 integers a and b and returns their diffrence
	>>> subtraction (55236525, 562702380)
	- 507465855
	'''
	return a - b

def multiplication(q, o):
    '''(int, int) -> (int)
    the function takes in two integers q and o and returns their product
    >>> multiplication (2, 2)
    4
    '''
    return q * o

def division (n, m):
    ''' (int, int) -> (float)
    the funtcion takes in two integers n and m and divides them
    >>> division (2, 2)
    1
    '''
    return n / m


    
def area (b, h, s):
    ''' (float, float, string) -> (float)
    the function takes in the base b and height h of a specified shape s and returns the area
    shapes: triangle, rectangle, square, paralellogram
    >>> area (9, 10, "triangle")
    45
    >>> area (20, 20, "rectangle")
    40
    '''
    if s == "triangle":
        return (b * h) /2

    elif s == "square" or s == "rectangle" or s == "paralellogram":
        return b * h
    else:
        return "Shape not defined"

    
    
def cubevol(b, w, h):
    ''' (float, float, float) -> (float)
    the function takes in the base b the height h and the width w of a cube and returns the volume
    >>> cubevol (2, 2, 2)
    6
    '''
    return b * w * h



    

addition()
subtraction()
multiplication()
division()
area()
cubevol()
