def armstrong():
    ##num = int(raw_input("Enter the positive number:"))#to verify the specific num
    for num in range(100,1000):
       result=0
       temp=num
        while temp>0:
            i=temp%10
            result+=i**3
            temp/=10
        
        if result==num:
            print "Entered number is armstrong",result
    
armstrong()
