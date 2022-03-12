n = 1
factor = 1
while factor <= n:
    if n % factor == 0:
        print(factor)
        factor += 1
        print()
        n += 1
        