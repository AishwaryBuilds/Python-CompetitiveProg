def maxkeep(n, a):
    if n <= 1:
        return n

    counter = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            counter += 1
    bes = counter

    for i in range(n-1):
        if a[i] == a[i+1]:
            continue

        delt = 0 

        if i > 0:
            old = 1 if a[i-1] != a[i] else 0
            new = 1 if a[i-1] != a[i+1] else 0
            delt += new - old

        if i+1 < n-1:
            old = 1 if a[i+1] != a[i+2] else 0
            new = 1 if a[i] != a[i+2] else 0
            delt += new - old

        bes = max(bes, counter + delt)

    return bes

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(maxkeep(n, a))


