def solution(n):
    answer = 0
    # n이 짝수인지
    if n%2==0:
       # n이 짝수
       for i in range(0, n+1, 2):
        answer += i
    else:
       # n이 홀수
       for j in range(0, n+1, 2):
        answer += j
    
    return answer