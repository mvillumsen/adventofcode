""" Part I """
print(sum(len(s[:-1]) - len(eval(s)) for s in open("../data/input08.txt")))

""" Part II """
print(sum(2+s.count("\\")+s.count('"') for s in open("../data/input08.txt")))
