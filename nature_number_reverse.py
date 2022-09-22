
def solution(n):
    n = str(n)
    answer = []
    for a in n:
        answer.append(int(a))
    answer.reverse()
    return answer

print(solution(12345))
