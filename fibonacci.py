n1 = 0
n2 = 1
count = 0
n = 14
print("Fibonacci sequence:")
while count < n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
