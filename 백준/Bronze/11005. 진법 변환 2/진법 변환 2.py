N, B = map(int, input().split())

nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

while N > 0:
  result += nums[N % B]
  N //= B

# 뒤집어서 출력
print(result[::-1])