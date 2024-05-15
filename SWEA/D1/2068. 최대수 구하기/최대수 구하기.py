T = int(input())
for test_case in range(1, T + 1):
    result = 0
    n = list(map(int, input().split()))
    print(f'#{test_case} {max(n)}')