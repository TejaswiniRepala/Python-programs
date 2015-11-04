def reverse(text):
    l=len(text)
    word=""
    for i in range(l):
        #print i
        #print l
        word += text[-i-1]
        #print word
    return word 
print reverse("sushma")
