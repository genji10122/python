while True:
    word = input("PICK A WORD")
    letter_list = []
    value = "yes"
    for num in range(len(word)-1):
        letter = word[num]
        if letter == "m" or letter == "M":
            value = "yes"
    if value == "no":
        print("TRUE")


    elif value == "yes":
        print("FALSE")
