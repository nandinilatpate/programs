# Program to print the first 10 Fibonacci numbers

a = 0
b = 1

print("First 10 Fibonacci numbers:")

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b