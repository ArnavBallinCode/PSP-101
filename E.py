

n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):  # ( start, stop, step)
    print(' ' * (n - i) + '*' * i)
