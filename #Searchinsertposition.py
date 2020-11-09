#search insert position.py
def searchInsert():
    nums=[1,2,3,4,5,6,9,10]
    target=5
    
    if len(nums)==0 and target==0:
        return 0

    for i in range(len(nums)):
        if target==nums[i]:
            return i
        
        elif target not in nums:
            if target < nums[i]:
                nums.insert(i,target)
                return i
    return i
print searchInsert()

