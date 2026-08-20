def dominotil(n, s):
    
    def choic(char):
        return [0, 1] if char == "?" else [int(char)]

    dblp = {}
    for i in choic(s[0]):
        for j in choic(s[1]):
            key = (i, j)
            dblp[key] = dblp.get(key, 0) + 1

    for pos in range(1, n - 1):
        ndblp = {}
        for (a, b), cnt in dblp.items():
            for c in choic(s[pos + 1]):
                old_wt = a + b
                new_wt = b + c
                if old_wt != new_wt:
                    key = (b, c)
                    ndblp[key] = ndblp.get(key, 0) + cnt
        dblp = ndblp

    return sum(dblp.values())
   

t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    print(dominotil(n, s))



