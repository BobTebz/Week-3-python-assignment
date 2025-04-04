
#User input
price =float(input("Please enter your price: "))
print("Price is R",price)

discount_percent=float(input("Please enter the discount amount: "))
print("Discount is",discount_percent,"%")

#Function
def my_function(price, discount_percent):
    if discount_percent >= 20 : 
        finalAmt =  price - (price * (discount_percent / 100))
        return print("Discounted amount = R",finalAmt)
    else:
        return print("No discount, price is R",price)

#Calling my function
my_function(price, discount_percent)

