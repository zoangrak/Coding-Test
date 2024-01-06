p = 0
maxP = 0

for _ in range(10):
  out_train, in_train = map(int, input().split())
  p += in_train - out_train
  maxP = max(p, maxP)

print(maxP)