#question 1

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
if a > b and a > c:
    print("The largest number is", a)
elif b > a and b > c:
    print("The largest number is", b)
else:
    print("The largest number is", c)

#question 2
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is a leap year")
else:    
    print("The year is not a leap year")

#question 3 - roots of quadratic equation 
equation = input("Enter a quadratic equation in the form of ax^2+bx+c: ")
a = int(equation[0])
b = int(equation[5])
c = int(equation[8])
d = (b**2) - (4*a*c)
if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print( root1, root2)
elif d == 0:
    root = -b / (2*a)
    print(root)
else:    
    real = -b / (2*a)
    imaginary = d**0.5 / (2*a)
    print(real, "+", imaginary, "i", real, "-", imaginary, "i")

#question 4 
num1 = float(input("Enter a number: ")) 
num2 = float(input("Enter another number: "))
if round(num1, 3) == round(num2, 3):
    print("same")
else:
    print("different")

#question 5 
char = input("Enter a character: ")
if len(char) > 1:
    print("Error")
elif char.isalpha() == False:
    print("Error")
elif char in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

# #question 6 

day = input("Enter a number between 1 and 7: ")
if day == "1":
    print("Monday")
elif day == "2":
    print("Tuesday")
elif day == "3":
    print("Wednesday")
elif day == "4":
    print("Thursday")
elif day == "5":
    print("Friday")
elif day == "6":
    print("Saturday")
elif day == "7":
    print("Sunday")
else:
    print("Error")

#question 7

num = int(input("Enter a number: "))
if num == 0:
    print("zero")
elif num > 0:
    print("positive")
    if abs(num) < 100:
        print("small")
    elif abs(num) > 1000:
        print("large")
else:
    print("negative")
    if abs(num) < 100:
        print("small")
    elif abs(num) > 1000:
        print("large")







