def youdel(stri):
	if "01" in stri:
		stri = stri.replace("01", "1", 1)
	else:
		idx = stri.rfind("0")
		stri = stri[:idx] + stri[idx + 1:]

	if "10" in stri:
		stri = stri.replace("10", "0", 1)
	else:
		idx = stri.rfind("1")
		stri =  stri[:idx] + stri[idx + 1:]

	return stri

t = int(input())
for _ in range(t):
	s = str(input())
	print(youdel(s))