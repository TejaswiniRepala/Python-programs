#Decompress Run-Length Encoded List.py

nums=[1,2,3,4]
new_n=[]

for i in range(len(nums)):
    new_n=new_n.insert(i,nums[i])
print new_n
