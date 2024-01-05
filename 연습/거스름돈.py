'''그리디 알고리즘'''
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  # 카운트
  count += n // coin
  # 나머지 n에 재할당
  n %= coin

print(count)