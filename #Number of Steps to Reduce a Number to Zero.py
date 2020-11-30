#Number of Steps to Reduce a Number to Zero.py

num=12

def numberOfSteps(num):
    count=0
    while num:
        if num%2==0:
            num/=2
        else:
            num-=1
        count+=1
    return count

print numberOfSteps(14)

