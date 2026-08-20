t = int(input())

for _ in range(t):
	n = int(input())
	a = [int(x) for x in input().split()]
	max_frost = []
	run_sum = 0
	min_avg = float('inf')
	for i in range(n):
		run_sum += a[i]
		min_avg = min(min_avg, run_sum // (i + 1))
		max_frost.append(min_avg)
	print(*max_frost)