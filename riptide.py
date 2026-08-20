t = int(input())
for _ in range(t):
    a, b, c = [int(x) for x in input().split()]
    nop = 0
    if a == b or b == c or c == a:
        print(nop)
    else:
        low, mid, hi = sorted([a, b, c])
        nop = min(mid - low, hi - mid)
        print(nop)

