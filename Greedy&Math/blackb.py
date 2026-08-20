def minrange(a, b, c):
    rangel = max(a, b, c) - min(a, b, c)
    range1 = max(b + c, b, c) - min(b + c, b, c)
    range2 = max(a, a + c, c) - min(a, a + c, c)
    range3 = max(a, b, a + b) - min(a, b, a + b)
    return min(rangel, range1, range2, range3)


t = int(input())
for _ in range(t):
    a, b, c = [int(x) for x in input().split()]
    print(minrange(a, b, c))

