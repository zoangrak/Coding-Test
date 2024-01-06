t = int(input())

for _ in range(t):
  A = list(map(int, input().split()))
  A.sort(reverse=True)
  print(A[2])