# a = '10'
# for i in a:
#     print(i)


def solution(a):
    a = str(a)
    b = [ int(x) for x in a]
    c = sum(b)
    if int(a) % c == 0:
        return True
    else:
        return False
print(solution(11))