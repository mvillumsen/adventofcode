import re

""" Part I """
inp = "3113322113"
c = 0

""" Part II """
#for i in range(50):
for i in range(40):
    tmp = ''
    while c < len(inp):
        letterCount = re.match(r'[%s]+' % inp[c], inp[c:]).end()
        tmp += str(letterCount) + inp[c]
        c += letterCount
    inp = tmp
    c = 0
print(len(inp))

