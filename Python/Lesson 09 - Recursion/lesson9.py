def factorial(n):
    if n == 1 or n == 0:
        print("best case reached")
        return 1
    print(f"computing factorial {n-1}")
    return n * factorial(n-1)

factorial(7)
