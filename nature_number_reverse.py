
def solution(n):
    n = str(n)
    answer = []
    for a in n:
        answer.append(int(a))
    answer.reverse()
    return answer

print(solution(12345))

#type 2
def solution(n):
    return list(map(int, reversed(str(n))))
