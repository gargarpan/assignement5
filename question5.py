num1 = float(input('Please enter a quantity: '))
print('quantity has entered', num1)
print("*****************")
total_cost=num1*100
print(" here the the total cost is************",total_cost)

if total_cost<1000 and total_cost>=100:
    print("sorry no discount for this amount*******")
    print("*******************")

    print("exact amount you have to pay************",total_cost)
    
    
elif total_cost>1000:

    discount=total_cost*10//100

    total=total_cost-discount

    
    print("Discount is ***** ",discount)
    print("***********************")
    print(" total cost after discount is  ****** ",total)    
    
    
    
    
    
else:
    print("sorry this is not for you***********")

    
