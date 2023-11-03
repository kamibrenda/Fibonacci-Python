"""The limit is the maximum value up to which we want to find even Fibonacci numbers."""
def even_fibonacci(limit):
    a, b = 1, 2
    even_fibs = []

    while a <= limit:
        if a % 2 == 0:
            even_fibs.append(a)
        a, b = b, a + b

    return even_fibs

limit = 10000  # Change this to the desired limit
even_fibs = even_fibonacci(limit)
print(even_fibs)
