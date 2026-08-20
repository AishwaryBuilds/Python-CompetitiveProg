t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    w = [input().strip() for _ in range(n)]
    a = [input().strip() for _ in range(m)]

    initials = set(word[0].upper() for word in w if word)

    all_valid = all(
        all(ch in initials for ch in candidate.upper())
        for candidate in a
    )
    print("YES" if all_valid else "NO")
