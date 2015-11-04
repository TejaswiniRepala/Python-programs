def leapyear():
    n=int(raw_input("Enter the leap year:"))
    if (n%4==0 and n%100!=0 or n%400==0):
        print 'It is a leap year'
    else:
        print 'It is not a leap year'
print leapyear()        
