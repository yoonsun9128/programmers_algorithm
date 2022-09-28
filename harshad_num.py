# a = '10'
# for i in a:
#     print(i)

#my solution
def solution(a):
    a = str(a)
    b = [ int(x) for x in a]
    c = sum(b)
    if int(a) % c == 0:
        return True
    else:
        return False
print(solution(a))

#other solution
def solution(a):
    b = sum([ int(x) for x in str(a)])
    if int(a) % b == 0:
        return True
    else:
        return False
print(solution(a))