from random import randint

def compare(u1, u2):

    pick = randint(0, 1)
    
    if pick == 0:
        answer = "Heads"
    if pick == 1:
        answer = "Tails"


##
##        
##    if u1 == 'Heads':
##        if answer == "Heads" :
##            return('OHHHH OH MY GOD AND ' + user1 + ' IS THE WINNNNEEEERRR')
##        
##        elif answer == "Tails":
##            return('OHHHH OH MY GOD AND ' + user2 + ' IS THE WINNNNEEEERRR')
##
##    if u1 == 'Tails':
##        if answer == "Heads" :
##            return('OHHHH OH MY GOD AND ' + user2 + ' IS THE WINNNNEEEERRR')
##        
##        elif answer == "Tails":
##            return('OHHHH OH MY GOD AND ' + user1 + ' IS THE WINNNNEEEERRR')
    
    
    if u1 == answer:
        return('OHHHH OH MY GOD AND ' + user1 + ' IS THE WINNNNEEEERRR')
    elif u2 == answer:
        return('OHHHH OH MY GOD AND ' + user2 + ' IS THE WINNNNEEEERRR')




while True:
    user1 = input("What's your name?")
    user2 = input("And your name?")
    user1_answer = input(user1  + " do you want to choose Heads or Tails?")

    if user1_answer == "Heads":
        user2_answer = "Tails"

    if user1_answer == "Tails":
        user2_answer = "Heads"

        
    print(compare(user1_answer, user2_answer))

