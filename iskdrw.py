t = int(input())
for _ in range(t):
	n = int(input())
	s = input().split("*")
	print((len(max(s)) + 1) // 2)