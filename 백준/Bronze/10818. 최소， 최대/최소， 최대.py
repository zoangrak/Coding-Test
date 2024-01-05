t = int(input())
n = list(map(int, input().split()))

minNum = n[0]
maxNum = n[0]
for i in range(t-1):
    if n[i+1] < minNum:
        minNum = n[i+1]
    if n[i+1] > maxNum:
        maxNum = n[i+1] 

print(minNum, maxNum)