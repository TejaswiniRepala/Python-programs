#Remove vowels from a string.py

def removevowels(str1):
#str1="bittunaniteju"
    v=['a','e','i','o','u','A','E','I','O','U']
    

    for i in str1:
        if i in v:
            str1= str1.replace(i,'')
    return str1



print removevowels("abdcebdefgihjABCESORU")



