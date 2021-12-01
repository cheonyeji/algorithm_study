def solution(mylist):
    answer = [[row[i] for row in mylist] for i in range(len(mylist))]
    # for i in range(len(mylist)):
    #     for row in mylist:
    #         print(row[i])
    new_list = list(map(list, zip(*mylist)))
    print(new_list)
    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
