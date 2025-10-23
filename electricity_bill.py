# Electricity Bill Calculator Program with Discount Feature
units = int(input("Enter units consumed: "))
rate_per_unit = 5

total_bill = units * rate_per_unit

print("Units Consumed:", units)
print("Total Bill: ₹", total_bill)

if total_bill > 1000:
    discount = total_bill * 0.10
    final_bill = total_bill - discount
    print("Discount Applied: ₹", discount)
    print("Final Bill: ₹", final_bill)
else:
    print("No discount applied.")
    print("Final Bill: ₹", total_bill)
