m = int(input())
n = int(input())

primes = [] # 소수 리스트
sum = 0
min_prime = 0

# m부터 n까지의 모든 수를 돌면서
for num in range(m, n+1):
  if num < 2:
    continue
  is_prime = True
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0: # 소수 아님
      is_prime = False
      break
  # 소수임. 리스트에 추가
  if is_prime:
    sum += num
    primes.append(num)

def print_result():
  if len(primes) == 0:
    print(-1)
    return
  print(sum)
  print(min(primes))
  
print_result()

