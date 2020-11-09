#mergetwolists.py

list1 = []
list2 = [1,4,6,7,9]

# sum_list=l1+l2
# final= sorted(sum_list)
# print final
i=j=0
current=[]

if (len(list1)==0 and len(list2)!=0):
    print list2

while i<list1 or j<list2:
    print "index:i,j",i,j
    

    if list1[i] <= list2[j]:
        #print list1[i]
        current.append(list1[i])
        i+=1
        
 
    elif list1[i] > list2[j]:
        current.append(list2[j])
        j+=1

    print "current list:",current

        #print list1
# if (list2!=0):
#     current.append(list1)
# else:
#     current.append(list2)

print type(current)


   

