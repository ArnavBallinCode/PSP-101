
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    space = n - i
    print(' ' * space + '*' * (2*i - 1))
