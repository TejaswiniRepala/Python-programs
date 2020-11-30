#Subtract the Product and Sum of Digits of an Integer.py

n=234
m=1
sum=0
result=0

for i in str(n):
    sum+=int(i)
    m*=int(i)
    result=m-sum
print result



    
    