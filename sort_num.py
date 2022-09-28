


from unittest import result


a = 118372

def solution(a):
    b = [x for x in str(a)]
    b.sort()
    b.reverse()
    result = ''.join(b)  #join을 사용할시 리스트 안에 있는 문자들이 str 이여야 한다!
    return int(result)
print(solution(118372))
