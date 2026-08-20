def bigram(k, c):
	max_c = max(c)
	cnt2 = sum(1 for x in c if x >= 2)
	if max_c >= 3 or cnt2 >= 2:
		print("YES")
	else:
		print("NO")

t = int(input())
for _ in range(t):
	k = int(input())
	c = [int(x) for x in input().split()]
	bigram(k, c)