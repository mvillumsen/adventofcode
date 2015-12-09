"""
Part I
"""

f = open("../data/input07.txt", "r").readlines()
c=i=0
d=dict()

while len(f) != 0:
	try:
		line = f[i].strip().split()
		
		if line[0] == "NOT":
			d[line[3]] = eval("~d[line[1]]&0xffff")
		elif line[1] == "AND":
			try:
				d[line[4]] = eval("int(line[0])&d[line[2]]")
			except:
				d[line[4]] = eval("d[line[0]]&d[line[2]]")
		elif line[1] == "OR":
			d[line[4]] = eval("d[line[0]]|d[line[2]]")
		elif line[1] == "RSHIFT":
			d[line[4]] = eval("d[line[0]]>>int(line[2])")
		elif line[1] == "LSHIFT":
			d[line[4]] = eval("d[line[0]]<<int(line[2])")
		else:
			# E.g. 123 -> x
			try:
				d[line[2]] = int(line[0])
			except:
				d[line[2]] = eval("d[line[0]]")
			"""
			# PART II START
			if line[-1] == 'b':
				d[line[-1]] = 956
			# PART II END
			"""
			
		del f[i]

	except:
		c += 1
		i = c%(len(f))

print(d['a'])
