#Remove duplicates from sorted array
def removeDuplicates():
    nums=[1,1,2]

    result=[]

    if len(nums)>0:
        for i in nums:
            if i not in result:
                result.append(i)
        #print type(result)
        return result,len(result)

print removeDuplicates()