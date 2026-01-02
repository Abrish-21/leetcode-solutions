def segments():
    m,n = map(int, input().split())
    arr = list(map(int, input().split()))
#
    l = 0
    count_segment = 0
    segment_sum = 0
    running_count = 0

    for r in range(m):
        segment_sum += arr[r] 

        while  segment_sum >= n:
            count_segment +=   m-r
            segment_sum -= arr[l]
            l += 1

        

    return count_segment
print(segments())
               