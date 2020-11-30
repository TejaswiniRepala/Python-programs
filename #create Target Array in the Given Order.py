#create Target Array in the Given Order.py

nums=[0,1,2,3,4]
index=[0,1,2,2,1]
new_n=[]

for i in range(len(nums)):
    new_n.insert(index[i],nums[i])
print new_n
