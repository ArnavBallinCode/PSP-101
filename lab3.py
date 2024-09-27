# Question 1: Identify Even or Odd
n = eval(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Question 2: Find the largest of two distinct numbers
n1 = eval(input("Enter the first number: "))
n2 = eval(input("Enter the second number: "))

if n1 > n2:
    print(f"{n1} is greater")
else:
    print(f"{n2} is greater")

# Question 3: Bob's Chocolate Calculation
n = eval(input("Enter money Bob has: "))
c = eval(input("Enter the price of each chocolate: "))
m = eval(input("Enter the number of wrappers for a free chocolate: "))

chocolates = n // c  # Total chocolates bought
free_chocolates = chocolates // m  # Free chocolates from wrappers

total_chocolates = chocolates + free_chocolates
print(f"Bob can eat {int(total_chocolates)} chocolates.")

# Question 4: Employee Net Salary Calculation
basic_pay = eval(input("Enter Basic Pay: "))
da_percentage = eval(input("Enter DA percentage: "))
hra_percentage = eval(input("Enter HRA percentage: "))
pf_percentage = eval(input("Enter PF percentage: "))

# Calculating the allowances and deductions
da = basic_pay * da_percentage / 100
hra = basic_pay * hra_percentage / 100
pf = basic_pay * pf_percentage / 100

# Net salary calculation
net_salary = basic_pay + da + hra - pf
print(f"Net Salary: {net_salary}")

# Question 5: Final Bill Calculation with Discounts
bill = eval(input("Enter the actual bill amount: "))
p1 = eval(input("Enter the P1 discount percentage: "))
p2 = eval(input("Enter the P2 discount percentage for bills >= 5000: "))

# Calculate P1 discount
discount_1 = bill * p1 / 100

# Additional discount if the bill is 5000 or more
if bill >= 5000:
    discount_2 = bill * p2 / 100
else:
    discount_2 = 0

# Final bill after both discounts
final_bill = bill - (discount_1 + discount_2)
print(f"Final amount to be paid: {final_bill}")
