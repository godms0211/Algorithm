N = int(input())
list_x = []
list_y = []

for i in range(N):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

a = (max(list_x) - min(list_x))* (max(list_y) - min(list_y))
print(a)