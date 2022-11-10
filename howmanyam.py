# my version
def solution(money):
    a = []
    count = money // 5500
    change = money % 5500
    a.append(count)
    a.append(change)
    return a

# another version
def solution(money):
    result = [money //5500, money%5500]
    return result