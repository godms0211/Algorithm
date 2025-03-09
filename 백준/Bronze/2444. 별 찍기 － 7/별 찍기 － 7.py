N = int(input())

for i in range(1, N):
  print(" " * (N - i) + '*' * (2*i - 1))

for h in range(N, 0, -1):
  print(" " * (N - h) + '*' * (2*h - 1))