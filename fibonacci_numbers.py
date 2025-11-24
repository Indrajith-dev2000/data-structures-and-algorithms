# Implementation using a for loop

n = int(input("Enter how many terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b



# Implementation using recursion

def fib(n):

    if n<=1:
        return n
    
    return fib(n-1) + fib(n-2)


n = int(input("Enter how many terms: "))
for i in range(n):
    print(fib(i), end=" ")