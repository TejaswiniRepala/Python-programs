#Jewels and Stones.py
J = "aA"
S = "aAAbbbb"

def JandS(J,S):
    count=0
    for i in S:
        if i in J:
            count +=1
    return count

print JandS("aA","aAAbbbb")
