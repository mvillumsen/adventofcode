import numpy as np
from time import time
""" Part I """
t1 = time()
f = open("../data/input06.txt", "r")
lights = np.zeros((1000,1000))
for line in f:
	line = line.split()

	p1x, p1y = int(line[-3].split(",")[0]), int(line[-3].split(",")[1])
	p2x, p2y = int(line[-1].split(",")[0]), int(line[-1].split(",")[1])

	if line[0] == 'toggle':
		lights[p1x:p2x+1:1,p1y:p2y+1:1] = 1 - lights[p1x:p2x+1:1,p1y:p2y+1:1]
	elif line[1] == 'on':
		lights[p1x:p2x+1:1,p1y:p2y+1:1] = 1

	elif line[1] == 'off':
		lights[p1x:p2x+1:1,p1y:p2y+1:1] = 0

print("Part I: {} total brightness".format(lights.sum()))
print("Time: %f seconds.\n"  % (time()-t1))
t2 = time()

""" Part II """
f = open("../data/input06.txt", "r")
lights = np.zeros((1000,1000))
for line in f:
	line = line.split()

	p1x, p1y = int(line[-3].split(",")[0]), int(line[-3].split(",")[1])
	p2x, p2y = int(line[-1].split(",")[0]), int(line[-1].split(",")[1])

	if line[0] == 'toggle':
		lights[p1x:p2x+1:1,p1y:p2y+1:1] += 2
	elif line[1] == 'on':
		lights[p1x:p2x+1:1,p1y:p2y+1:1] += 1

	elif line[1] == 'off':
		lights[p1x:p2x+1:1,p1y:p2y+1:1] -= 1
		lights[lights < 0] = 0

print("Part II: {} total brightness".format(lights.sum()))
print("Time: %f seconds."  % (time()-t2))