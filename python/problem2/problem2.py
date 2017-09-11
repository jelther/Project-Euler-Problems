def fibonacci(n):
    if (n == 0): return 0
    if (n in [1,2]): return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

total_sum = 0
for x in xrange(1,101,3):

    fib = fibonacci(x)
    if (fib % 2 != 0):
        total_sum = total_sum + fib

print total_sum