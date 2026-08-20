def nikibk(n, a):
    an = a[:len(a)]
    i = 1
    for u in range(len(an) - 1):
        while an[u] >= 1 and an[u] > an[u + 1]:
            an[u + 1] += i
            an[u] -= i
            i += 1
    for num in an:
        if an[u + 1] - an[u] >= 1:
            pass
        else:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    nikibk(n, a)
