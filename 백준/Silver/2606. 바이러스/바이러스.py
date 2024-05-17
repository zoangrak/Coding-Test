def dfs(idx):
    global visited, cnt
    visited[idx] = True
    cnt += 1
    for next in range(1, n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

# 0. 입력 및 초기화
n = int(input()) # pc 갯수
m = int(input()) # 연결된 pc 쌍의 수

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

# 1. graph 정보 입력
for _ in range(1, m+1):
    a, b = map(int, input().split()) # 번호 쌍
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs
dfs(1)
print(cnt-1)