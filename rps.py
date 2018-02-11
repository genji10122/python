import getpass



def compare(u1, u2):
    if u1 == u2:
        print('OHHH AND ITS A TIEEE!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    
    if u1 == 'rock':
        if u2 == 'scissors':
            return('OHHHH OH MY GOD AND ' + user1 + ' IS THE WINNNNEEEERRR')
        elif u2 == 'paper':
            return('OHHHH OH MY GOD AND ' + user2 + ' IS THE WINNNNEEEERRR')
    

    if u1 == 'paper':
        if u2 == 'scissors':
            return('OHHHH OH MY GOD AND ' + user2 + ' IS THE WINNNNEEEERRR')
        elif u2 == 'rock':
            return('OHHHH OH MY GOD AND ' + user1 + ' IS THE WINNNNEEEERRR')

    if u1 == 'scissors':
        if u2 == 'rock':
            return('OHHHH OH MY GOD AND ' + user2 + ' IS THE WINNNNEEEERRR')
        elif u2 == 'paper':
            return('OHHHH OH MY GOD AND ' + user1 + ' IS THE WINNNNEEEERRR')


while True:
    user1 = input("What's your name?")
    user2 = input("And your name?")
    user1_answer = getpass.getpass(user1  + " do you want to choose rock, paper or scissors?")
    user2_answer = getpass.getpass(user2  + " do you want to choose rock, paper or scissors?")
    print(compare(user1_answer, user2_answer))
