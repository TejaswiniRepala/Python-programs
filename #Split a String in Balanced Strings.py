#Split a String in Balanced Strings.py

s="RLRRRLLRLL"

num_L=num_R=count=0

for i in s:
    if i=='L':
        num_L+=1
    elif i=='R':
        num_R+=1
    if num_L==num_R:
        count+=1
print count

