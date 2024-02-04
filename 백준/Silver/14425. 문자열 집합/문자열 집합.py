import sys

n, m = map(int, sys.stdin.readline().split())

s = dict()
cnt = 0

for _ in range(n):
  word = sys.stdin.readline()
  s[word] = True

for _ in range(m):
  chk = sys.stdin.readline()
  if chk in s.keys():
    cnt += 1

print(cnt)