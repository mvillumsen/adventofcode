""" Part I """
f = open("../data/input01.txt").readlines()
c=0
for ch in f[0]:
	if ch == '(':
		c += 1
	else:
		c -= 1
print(c)

""" Part II """
c=0
for i in range(len(f[0])):
	ch = f[0][i]
	if ch == '(':
		c += 1
	else:
		c -= 1
	if c < 0:
		break
print(i+1)
