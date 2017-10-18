def factor(i):
    if (i < 0):
        return 0
    p = 1
    for j in range(1, i + 1):
        p *= j
    return p


perm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(perm)
perm_num = ''
remain = 1000000 - 1

numbs = []
for i in range(n):
    numbs.append(i)

for i in range(1, n):
    j = remain / factor(n - i)
    remain = remain % factor(n - i)
    perm_num += str(numbs[j])
    numbs.remove(numbs[j])
    if (remain == 0):
        break

for numb in numbs:
    perm_num += str(numb)

print perm_num