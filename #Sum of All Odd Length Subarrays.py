#Sum of All Odd Length Subarrays.py
arr = [1,4,2,5,3]
new_arr=[]

n=len(arr)

for i in range(0,n,3):
    new_arr=arr[i:i+n]
print new_arr

