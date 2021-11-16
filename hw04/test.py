def max_part(n):
    i = 0
    while n != 0:
        if n == 1:
            break
        n = n//2
        i += 1
    return pow(2,i)
