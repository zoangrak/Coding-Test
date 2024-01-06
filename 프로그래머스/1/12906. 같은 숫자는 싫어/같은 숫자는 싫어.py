def solution(arr):
    result = []
    
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1] : # 첫번재 숫자거나 이전 숫자와 다른 경우
            result.append(arr[i])
    return result