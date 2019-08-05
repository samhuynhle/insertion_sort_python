testlist1 = [8,9,10,2,3,6,4,5,1,7]
def insertion_sort(some_list):
    count = 0
    for x in range(1, len(some_list), 1):
        for j in range(x, 0, -1):
            if some_list[x-j] > some_list[x]:
                count += 1
                some_list[x], some_list[x-j] = some_list[x-j], some_list[x]
    print(count)
    print(some_list)
insertion_sort(testlist1)
