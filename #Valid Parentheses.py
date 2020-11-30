#Valid Parentheses.py
#def isValid():
s="(){}[](}"

list1=[]

def isValid():



    for i in range(len(s)):
        if s[i]=='{' or s[i]=='[' or s[i]=='(':
            list1.append(s[i])
        else:
            if len(list1)==0:
                return ""
            op=list1.pop()
            a=s[i]
            if (op=='(' and a==')') or (op=='{' and a=='}') or (op=='[' and a==']'):
                return True,op,a
            else:
                return False,op,a
    return len(list1)==0
print isValid()