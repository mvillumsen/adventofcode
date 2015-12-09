""" Part 1 """
f = open("../data/input03.txt", "r").readlines()
row=col=0
santa=set()
for line in f:
	for c in line:
		santa.add((row,col))
		if c == '>':
			col += 1
		elif c == '<':
			col -= 1
		elif c == '^':
			row += 1
		elif c == 'v':
			row -= 1

print("Part 1: ", len(santa))


""" Part 2 """
f = open("../data/input03.txt", "r").readlines()
counter=row1=row2=col1=col2=0
robo=santa=set()
for line in f:
	for c in line:
		if (counter % 2) == 0:
			santa.add((row1,col1))
			if c == '>':
				col1 += 1
			elif c == '<':
				col1 -= 1
			elif c == '^':
				row1 += 1
			elif c == 'v':
				row1 -= 1
		else:
			robo.add((row2,col2))
			if c == '>':
				col2 += 1
			elif c == '<':
				col2 -= 1
			elif c == '^':
				row2 += 1
			elif c == 'v':
				row2 -= 1
		counter += 1
print("Part 2: ", len(robo.union(santa)))
