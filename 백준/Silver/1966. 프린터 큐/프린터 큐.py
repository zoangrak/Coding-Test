case = int(input())

for _ in range(case):
  n, m = map(int, input().split())
  priority = list(map(int, input().split()))
  count = 0
  
  # N개 문서의 기존 순서 저장
  index = [i for i in range(n)]

  while True:
    if priority[0] == max(priority):
      count += 1
      if index[0] == m:
        print(count)
        break
      else:
        del priority[0]
        del index[0]
    else:
      priority.append(priority[0])
      del priority[0]
      index.append(index[0])
      del index[0]