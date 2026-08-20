def divaconq(x, y):
	if x < y:
		print("NO")
		return
	if x == y:
		print("YES")
		return
	else:
		for i in range(1, x + 1):
			if x / i == y:
				print("YES")
				return
	if x != y:
		print("NO")
		return

t = int(input())
for _ in range(t):
	x, y = [int(a) for a in input().split()]
	divaconq(x, y)