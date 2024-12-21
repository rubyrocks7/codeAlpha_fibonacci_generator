def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
fib_gen = fibonacci_generator()

# Generate the first 10 Fibonacci numbers
for _ in range(20):
    print(next(fib_gen))
# Generator Function: fibonacci_generator uses the yield keyword to return values one at a time, preserving the function's state between calls.
# Infinite Sequence: This generator runs indefinitely, so you can call next() on it as many times as you need.
9