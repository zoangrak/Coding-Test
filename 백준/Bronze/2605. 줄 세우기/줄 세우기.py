import sys
input = sys.stdin.readline

n = int(input())
st = []
lst = list(map(int, input().split()))

for i in range(n):
  if lst[i] == 0:
    st.insert(0, i+1)
  else:
    st.insert(lst[i], i+1)

for i in reversed(st):
  print(i, end=' ')