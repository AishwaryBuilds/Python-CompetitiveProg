def maxscr(tn):
    nonempt = tn
    score = 0
    while nonempt:
        frst = {}
        lst = {}
        for idx, num in enumerate(nonempt):
            if num not in frst:
                frst[num] = idx
            lst[num] = idx

        best_num, best_size = None, -1
        for num in frst:
            size = lst[num] - frst[num] + 1
            if size > best_size:
                best_size, best_num = size, num

        score += best_size ** 2
        l, r = frst[best_num], lst[best_num]
        nonempt = nonempt[:l] + nonempt[r + 1:]
    return score

t = int(input())
for _ in range(t):
    n = int(input())
    tn = [int(x) for x in input().split()]
    print(maxscr(tn))
