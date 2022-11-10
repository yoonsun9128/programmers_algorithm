# version 1
def solution(a):
    answer = a[::-1]
    return answer

# version 2
def solution(a):
    answer = "".join(reversed(a))
    return answer