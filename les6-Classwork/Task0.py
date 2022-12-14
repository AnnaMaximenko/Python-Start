# sp1 = [1, 2, 3, 4, 5, 6]
# sp2 = [10, 20, 30, 40]
# for i, j in zip(sp1, sp2):
#     print (i, j)

# sp = ['a', 'b', 'c']
# for i, el in enumerate(sp, 1):
#     print(i, el)

def prime(n):
    res = []
    d = 2
    while d <= n ** 0.5:
        if n % d == 0:
            res.append(d)
            k = n // d
            if k != d:
                res.append(k)
        d += 1
    return not res

print(prime(110))