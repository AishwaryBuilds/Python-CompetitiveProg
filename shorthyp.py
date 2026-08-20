from itertools import groupby

def hyperc():
    n = int(input())
    a = [int(x) for x in input().split()]

    counter = len(list(groupby(a)))

    for i in range(n - 1):
        a[i], a[i + 1] = a[i + 1], a[i]

        counter = max(counter, len(list(groupby(a))))

        a[i], a[i + 1] = a[i + 1], a[i]

    return counter

t = int(input())
for _ in range(t):
    print(hyperc())
