def mergeSort():
    n,m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    p1,p2 = 0,0

    merge_sort = []
    while p1 < n and p2 < m:
        if arr1[p1] < arr2[p2]:
            merge_sort.append(arr1[p1])
            p1 += 1
        elif arr2[p2] < arr1[p1]:
            merge_sort.append(arr2[p2])
            p2 += 1
        else:
            merge_sort.append(arr1[p1])
            merge_sort.append(arr2[p2])
            p1  += 1
            p2  += 1
    # if there is a remaing number in one of the two arrays
    if p1 < n:
        merge_sort.extend(arr1[p1:])
    if p2 < m:
        merge_sort.extend(arr2[p2:])

    return ' '.join(map(str, merge_sort))
print(mergeSort())




