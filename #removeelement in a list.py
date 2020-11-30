#removeelement in a list.py


def removeelement(val):
    nums=[3,2,2,3]
    a=len(nums)

    result=[]
    if a>0:
        for i in nums:
            if i!=val:
                print i
                result.append(i)
        print len(result)

print removeelement(3)

    