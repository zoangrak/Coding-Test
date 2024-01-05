t = int(input())

for _ in range(t):
    n = int(input())
    binaryNum = format(n, 'b')
    position = [i for i in range(len(binaryNum))
        if binaryNum[-i-1] == '1']
    print(*position)