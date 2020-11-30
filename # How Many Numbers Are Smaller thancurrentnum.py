# How Many Numbers Are Smaller Than the Current Number.py

nums=[8,1,2,2,3]

new_nums=[]

for i in range(len(nums)):
    count=0
    for j in range(len(nums)):
        if nums[i]> nums[j]:
            count+=1
    new_nums.append(count)
print new_nums
