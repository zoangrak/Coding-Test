from collections import deque

def bfs(n, k):
    visited = [False] * 100001
    q = deque([(n, 0)])

    while q:
        cur, time = q.popleft()
        if cur == k:
            return time
        for next in (cur-1, cur+1, cur*2):
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = True
                q.append((next, time+1))
    return -1

n, k = map(int, input().split())
print(bfs(n, k))