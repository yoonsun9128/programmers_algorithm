def solution(a):
    b=[]
    for a in range(a+1):
        if a % 2 == 0:
            b.append(a)
    result = sum(b)
    print (result)

solution(4)