from hashlib import md5

"""
Part 1
"""
s = open("../data/input04.txt").readlines()[0].strip()
c = 0
while (md5(s.encode('utf-8')+str(c).encode('utf-8')).hexdigest()[0:5] != "00000"):
	c += 1
print(c)


"""
Part 2
"""

c = 0
while (md5(s.encode('utf-8')+str(c).encode('utf-8')).hexdigest()[0:6] != "000000"):
	c += 1
print(c)
