'''Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].'''

nums = [2,5,1,3,4,7]
n = 3
nums1=[]
nums2=[]
result=[]
def shuffle():

    for i in range(0,len(nums)):
        #print i
        if i < n:
            nums1.append(nums[i])
        else:
            nums2.append(nums[i])


    for i,j in zip(nums1,nums2):
        result.append(i)
        result.append(j)

    return result

print shuffle()
