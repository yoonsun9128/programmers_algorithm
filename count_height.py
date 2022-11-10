def solution(array, height):
    count = 0
    for a in array:
        if a < height:
            pass
        else:
            count += 1
    return count