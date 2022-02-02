# nth fibonacci number

fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
print(fib(7))
