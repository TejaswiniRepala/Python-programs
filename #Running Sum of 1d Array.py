#Running Sum of 1d Array.py

nums=[1,2,3,4]

new_nums=[]
count=0

for i in range(len(nums)):
    count+=nums[i]
    new_nums.append(count)
print new_nums
