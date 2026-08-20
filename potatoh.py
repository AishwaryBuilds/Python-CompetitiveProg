def potatoh(n, k, s):
    s = list(s)
    size = 2 * n
    while k > 0:
        for i in range(size):
            idx = i % size
            prev = (i - 1) % size
            if s[idx] == "0" and s[idx - 1] != "0" and s[idx - 1] == "1":              
                s[idx] == "1"
                s[prev] == "0"
            else:
                s[idx] = "0" if s[(idx + 1) % size] != "0" else "1"
                s[prev] = "1"
            k -= 1
            if k == 0:
                break


    bluet = s[::2]
    redt = s[1::2]
    bluets = redt.count("0")
    redts = bluet.count("0")
    return int(redts), int(bluets)


t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    s = str(input())
    print(*potatoh(n, k, s))




