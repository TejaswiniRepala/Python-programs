#RomanToInt
def RomanToInt(num):
    dict_num={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0

    for i in range(len(num)):
        if i+1 == len(num) or dict_num[num[i+1]] <= dict_num[num[i]]:
            total += dict_num[num[i]]
        else:
            total -= dict_num[num[i]]
    return total

    #total = [total+dict_num[num[i]] for i in range(len(num)) if i+1 == len(num) or dict_num[num[i+1]] <= dict_num[num[i]]]

print RomanToInt("LCXMD")
