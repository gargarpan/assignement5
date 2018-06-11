num1 = int(input('Please enter a year: '))
print('year has entered', num1)

if num1%4==0 and num1%100 !=0:
    
        print("this is a leap year")
elif num1%100==0:
        print("not a leap yaer")
elif num1%400==0:
    print("this is a leap year")
else:
    print("not a leap yaer")
    
        
