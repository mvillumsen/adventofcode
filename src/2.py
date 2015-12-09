import functools
c=0
f = open("../data/input02.txt","r")
for line in f:
	line = line.replace("\n","").split("x")
	tmp = [int(line[0]), int(line[1]), int(line[2])]
	ribbon = functools.reduce(lambda x, y: x*y, tmp)
	#c += sum([a*2 for a in tmp]) + min(tmp)
	a = min(tmp)
	tmp.remove(a)
	b = min(tmp)
	c += 2*a + 2*b + ribbon

print(c)
