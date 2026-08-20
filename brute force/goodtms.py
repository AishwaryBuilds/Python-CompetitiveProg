def goodtms(x):
	y = 2
	while True:
		goodint = x * y
		uniqstr = set(str(goodint))
		if len(uniqstr) <= 2 and len(set(str(y))) <= 2:
			return y
		else:
			y += 1

t = int(input())

for _ in range(t):
	x = int(input())
	print(goodtms(x))