a = ["We", "are", "the", "world!"]

def solution(a):
    b = []
    c = []
    for i in a:
       b.append(i)
    for e in b:
        c.append(len(e))
    return c

print(solution(a))
