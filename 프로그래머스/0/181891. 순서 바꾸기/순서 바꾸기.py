def solution(num_list, n):
    answer = []
    answer2 = []
    for i, num in enumerate(num_list):
        if i < n:
            answer.append(num_list[i])
        else:
            answer2.append(num_list[i])
            
    return answer2 + answer