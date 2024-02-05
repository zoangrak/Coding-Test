n, x = map(int, input().split())
li = list(map(int, input().split()))

if not (1 <= x <= n <= 250000):
  exit()

if max(li) == 0:
  print("SAD")
else:
  max_sum = sum(li[0:x])
  value = max_sum
  cnt = 1
  for i in range(x, n):
    value -= li[i-x]
    value += li[i]
    if value > max_sum:
      max_sum = value
      cnt = 1
    elif value == max_sum:
      cnt += 1

  print(max_sum)
  print(cnt)
