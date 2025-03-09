T = int(input())
l = []

for i in range(T):
    k = str(input())
    l.append(k[0] + k[-1])

for j in range(T):
    print(l[j], end=' ')
