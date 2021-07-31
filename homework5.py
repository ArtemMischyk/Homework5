def addNum(seq, num):
    seq = list(seq)
    for i in range(len(seq)):
        seq[i] += num
    return seq

origin = (3, 6, 2, 6)
changed = addNum(origin, 3)

print(origin)
print(changed)




















l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])





















a = {0, 1, 2, 3}
b = {4, 3, 2, 1}
c = a.intersection(b)
print(c)



















x = {1, 2, 3}
y = {4, 3, 6}
z = y.clear()
print(y)


















l1 = [10, 20, 30, 40, 50]
l2 = [50, 75, 30, 20, 40, 69]

res = [x for x in l1 + l2 if x not in a or l1 not in l2]
print(res)
a.difference(l2)