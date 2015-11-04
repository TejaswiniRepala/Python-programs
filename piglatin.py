VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
def word():
    phrase = raw_input("Enter a word in English:")
    if len(phrase)>0 and phrase.isalpha():
         return phrase
    else:
        exit(0)
#(or)print "empty"        
def piglatin():
    phrase = word()
    print phrase
    if phrase[0] in VOWELS:
        print phrase + "ay"
    else:
        print phrase[1:] + phrase[0] +"ay"

piglatin()
