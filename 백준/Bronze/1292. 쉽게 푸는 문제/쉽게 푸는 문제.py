a, b = map(int, input().split())
data = []

for i in range(1, b+1):
  for j in range(i):
    data.append(i)

result = sum(data[a-1 : b])

print(result)