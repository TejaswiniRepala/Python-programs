def remove_duplicates(elements):
    numbers=[]
    for i in elements:
        if i not in numbers:
            numbers.append(i)
    return numbers
print remove_duplicates([1,1,2,8,7,2,7,0,4,3,6,4,0,6])    
