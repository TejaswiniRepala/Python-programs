#Kids With the Greatest Number of Candies.py
def kidsWithCandies(candies, extraCandies):
    # candies = [2,3,5,1,3]
    # extraCandies = 3
    result=[]
    max_candy=max(candies)


    for i in candies:
        if (i+extraCandies) >= max_candy:
           result.append(True)
        else:
            result.append(False)
    return result

print kidsWithCandies([2,3,5,1,3],3)