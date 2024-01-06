n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
  if num == 1:
    continue
  is_prime = True
  for i in range(2, int(num ** 0.5)+1):
    if num % i == 0: # 소수가 아님
      is_prime = False
      break
  if is_prime:
    cnt += 1

print(cnt)