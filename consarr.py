t = int(input())

for _ in range(t):
	n = int(input())
	res_arr = []
	for i in range(2 * n):
		if i % 2 == 1:
			res_arr.append(i)
		else:
			pass
	print(*res_arr)