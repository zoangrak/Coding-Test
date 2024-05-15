T = int(input())
for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    if (n[0] > n[1]):
        sign = '>'
    if (n[0] < n[1]):
        sign = '<'
    if (n[0] == n[1]):
        sign = '='

    print(f'#{test_case} {sign}')