T = 10
for tc in range(1, T+1):
    n = int(input())
    res = 0

    graph = [list(map(int, input().split())) * n for _ in range(n)]

    for i in range(n):
        flag = 0
        for j in range(n):
            if graph[j][i] == 1:
                flag = 1
            elif graph[j][i] == 2:
                if flag:
                	res += 1
                	flag = 0

    print(f'#{tc} {res}')