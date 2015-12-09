"""
Part I

Contains at least three vowels (only 'aeiou').
Contains at least one letter that appears twice in a row,
e.g. abcdde (dd).
Does not contain the strings 'ab', 'cd', 'pq' or 'xy'
"""

vowels = "aeiou" # At least three vowels
notContain = ["ab","cd","pq","xy"] # Does not contain
words = 0
f = open("../data/input05.txt", "r")

for line in f:
	v = count = 0
	twoInaRow = False
	contains = False
	
	for s in notContain:
		if s in line:
			contains = True

	for c in line:
		if c in vowels:
			v += 1

	for i in range(len(line)-1):
		if line[i] == line[i+1]:
			twoInaRow = True
	
	if twoInaRow and not contains and v >= 3:
		words += 1

print(words)


"""
Part II

Contains a pair of any two letters that appear at least twice without overlapping,
e.g.xyxy (xy) but not aaa* (aa).
Contains a least one letter which repeats with exactly one letter between them,
e.g. xyx (x) and aaa (a).
"""

f = open("../data/input05.txt", "r")
words = 0
for line in f:
	repeat = False
	pair = False
	for i in range(len(line)-1):
		for j in range(i+2, len(line)-1):
			if line[j:j+2] == line[i:i+2]:
				pair = True

	for k in range(len(line)-2):
		if line[k] == line[k+2]:
			repeat = True

	if repeat and pair:
		words += 1

print(words)
