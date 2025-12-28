N = int(input())
list = []

for _ in range(N):
  list.append(int(input()))

list.sort()

for n in list:
  print(n)