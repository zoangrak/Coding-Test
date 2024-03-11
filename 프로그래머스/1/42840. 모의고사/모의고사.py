def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a = 0
    s1, s2, s3 = 0, 0, 0
    
    for i in answers:
        if i==a1[a%5]: s1+=1
        if i==a2[a%8]: s2+=1
        if i==a3[a%10]: s3+=1
        a+=1
    
    k = max(s1, s2, s3)
    
    if(k==s1): answer.append(1)
    if(k==s2): answer.append(2)
    if(k==s3): answer.append(3)
    
    return answer
    
    
    