              
def findpairs_sum(nums,k):
    result=[]
    while nums:
        num=nums.pop()
        diff=k-num
        if diff in nums:
            result.append((diff,num))
    return result

print findpairs_sum([10,15,3,7],17)