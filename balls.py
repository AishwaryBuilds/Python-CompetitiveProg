n = int(input())
N = [int(x) for x in input().split()]
counter = 0
while N:
    indi_dict = {}
    for i, val in enumerate(N):
        if val not in indi_dict:
            indi_dict[val] = []
        indi_dict[val].append(i)
        for i in range(i):
            for key, value in indi_dict:






