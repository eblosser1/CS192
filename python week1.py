print("Welcome to the Express Lane!")
price1 = float(input("Enter the first price: "))
price2 = float(input("Enter the second price: "))
price3 = float(input("Enter the third price: "))
price4 = float(input("Enter the fourth price: "))
price5 = float(input("Enter the final price: "))
subtotal = price1 + price2 + price3 + price4 + price5
print("subtotal:", subtotal)
tax = round(subtotal * .06, 2)
print("sales tax:", tax)
print("-------------------")
total = subtotal + tax
print("total:", total)