def solution(list_of_nums):
    e = 0
    o = 0
    d = {}
    for i in list_of_nums:
        if(i % 2 == 0):
            e = e + 1
        else:
            o = o + 1

    d['ODD'] = o
    d['EVEN'] = e
    return d

solution([1, 2, 3, 5, 8, 9])
