t = int(input())

for _ in range(t):
	n = int(input())
	a = [int(x) for x in input().split()]

	breaks = []
	diff = []
	for i in range(n - 1):
		if a[i] > a[i + 1]:
			diff.append(a[i] - a[i + 1])
			breaks.append(i)

	if len(breaks) == 0:
		print("YES")
		continue

	k = max(diff)

	split = breaks[0] + 1

	labels = [0] * n
	labels[split] = 1

	valid = True

	for i in range(split + 1, n):
		prev = a[i - 1] + k * labels[i-1]

		if prev <= a[i]:
			labels[i] = 0
		elif prev <= a[i] + k:
			labels[i] = 1
		else:
			valid = False
			break

	if not valid:
		print("NO")
		continue

	res_arr = [a[i] + k * labels[i] for i in range(n)]
	print("YES" if res_arr == sorted(res_arr) else "NO")



