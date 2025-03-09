n = int(input())
area = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y =map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            area[i][j] = 1

total = 0
for k in range(100):
    total += area[k].count(1)

print(total)