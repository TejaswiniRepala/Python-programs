def AskForLetter():

    while True:
        letter=raw_input('Enter the letter; type "quit" to end.\n')

        if letter == 'quit':
            exit()
        try:
            len(letter) == 1
            print ("The length of the letter is 1")
            IsVowel(letter)
        except:
            print("The length of the letter is not equal to 1:")
         
def IsVowel(letter):

    var==AskForLetter()

    if(var=="a" or var=="e" or var=="i" or var=="o" or var=="u"):

        print ("The letter is lowercase vowel:")

        IsLowercaseVowel(letter)

        return True

    elif(var=="A" or var=="E" or var=="I" or var=="O" or var=="U"):

        print ("The letter is uppercase vowel:")

        IsUppercaseVowel(letter)

        return False 

    else:

        print("The given letter is not a vowel:")

    

def IsLowercaseVowel(letter):

    print ("The letter is lowercase vowel:")

    return True

def IsUppercaseVowel(letter):

    print ("The letter is uppercase vowel:")

    return False
