def solution(array, n):
    count = 0
    for a in array:
        if a == n:
            count +=1
    return count

solution([1, 1, 2, 3, 4, 5], 1)