#shufflestring.py

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
new_s=[""]*len(s)

for i in range (len(s)):
    new_s[indices[i]]=s[i]
print "".join(new_s)
