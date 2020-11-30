#XOR Operation in an Array.py

n=10
start=5
nums=[]
count=0

for i in range(n):
    nums.insert(i,start+2*i)
    count^=nums[i]
print count