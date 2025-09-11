from datetime import datetime

DISCOUNT_DAYS = [1,2]  # Monday=1, Tuesday=2
DISCOUNT_RATE = 0.1
SALES_TAX_RATE = 0.06

discount = 0
quantity = 1
subtotal = 0
today = datetime.now()
day_of_week = today.weekday()

while quantity != 0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:
        price = float(input("Enter the price: "))
        subtotal += quantity * price 

print("---Your Order---")
print(f"Subtotal:  ${subtotal:.2f}:")
if day_of_week in DISCOUNT_DAYS:
    if subtotal >= 50:
        discount = round(subtotal * DISCOUNT_RATE, 2)
        subtotal -= discount
        print(f"Discount:  ${discount:.2f}")
    else: 
        short = 50 - subtotal
        print(f"You are ${short:.2f} way from getting a discount!")

tax = round(subtotal * SALES_TAX_RATE, 2)
total = subtotal + tax

print(f"Sales Tax: ${tax:.2f}")
print(f"Total Amount Due: ${total:.2f}")

