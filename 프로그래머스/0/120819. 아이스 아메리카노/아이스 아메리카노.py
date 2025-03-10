def solution(money):
    answer = []
    moneynumber = money // 5500
    answer.append(moneynumber)
    answer.append(money-moneynumber*5500)
    return answer