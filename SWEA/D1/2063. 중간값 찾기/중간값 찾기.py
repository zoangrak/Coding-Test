T = int(input())
for test_case in range(1, T + 1):
    try:
        n = sorted(list(map(int, input().split())))
        answer = n[T//2]
        print(answer)
    except:
        break