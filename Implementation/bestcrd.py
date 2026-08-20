def potatoh(n, k, s):
    s = list(s)
    size = 2 * n

    i = 0
    while k > 0:
        idx = i % size
        s[idx] = "1" if s[idx] == "0" else "0"
        i += 1
        k -= 1

    bluet = s[::2]   # even indices
    redt = s[1::2]   # odd indices

    red_score = bluet.count("0")   # red's score = zeroes in blue team
    blue_score = redt.count("0")   # blue's score = zeroes in red team

    return red_score, blue_score


t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    s = input()
    print(*potatoh(n, k, s))