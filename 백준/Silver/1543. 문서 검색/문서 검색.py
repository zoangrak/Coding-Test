import sys
input = sys.stdin.readline

s = input().strip()
x = input().strip()

cnt = 0
i = 0

while i < len(s):
  if s[i:i+len(x)] == x:
    i += len(x)
    cnt += 1
  else:
    i += 1

print(cnt)