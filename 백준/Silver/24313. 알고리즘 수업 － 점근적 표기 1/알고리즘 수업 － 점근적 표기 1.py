a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if (a1*n0 + a0) <= (n0*c) and (a1 <= c):
    print(1)
else:
    print(0)