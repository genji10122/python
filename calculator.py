##
##import sys
##from PySide.QtCore import *
##from PySide.QtGui import *
##

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

def run_calculator():
        while True:
                operation = input("What function do you want to perform? ")
                first_number = int(input("What number would you like to choose?"))

                second_number = int(input("What number would you like to choose?"))

                if operation == "Addition":
                        ## use "Addition"
           
                        print(addition(first_number, second_number))
                
                elif operation == "Subtraction":
                        ## use "Subtraction"
                
                   print(subtraction(first_number, second_number))


                elif operation == "Multiplication":
                        ## use "Multiplication"
                
                        print(multiplication(first_number, second_number))


                elif operation == "Division":
                        ## use "Division"
                        
                        print(division(first_number, second_number))

                
                else:
                        print("SORRY NOT APPLICABLE")
                
                

run_calculator()


#### Addition Subtraction Multiplication Division
##app = QApplication(sys.argv)    
##run_calculator()
### Create a button
##buttona = QPushButton("Add")
##buttons = QPushButton("Subtract")
##buttond = QPushButton("Divide")
##buttonm = QPushButton("Multiply")
##
##
##buttona.clicked.connect(addition)
##buttons.clicked.connect(subtraction)
##buttond.clicked.connect(division)
##buttonm.clicked.connect(multiplication)
##button.show()
### Run the main Qt loop
##app.exec_()
##
##







