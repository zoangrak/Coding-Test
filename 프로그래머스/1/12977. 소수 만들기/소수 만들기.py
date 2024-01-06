from itertools import combinations

def solution(nums):
    cnt = 0
    data = list(combinations(nums, 3))
    sums = [sum(comb) for comb in data]
    
    for s in sums:
        is_prime = True
        for i in range(2, s):
            if s % i == 0:
                is_prime = False
                break
        if s > 1 and is_prime:
            cnt += 1
    
    return cnt