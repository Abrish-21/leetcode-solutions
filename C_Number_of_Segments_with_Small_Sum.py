def segments():
    m,n = map(int, input().split())
    arr = list(map(int, input().split()))

    l = 0
    count_segment = 0
    segment_sum = 0

    for r in range(m):
        segment_sum += arr[r]

        while  segment_sum > n:
            segment_sum -= arr[l]
            l += 1

        count_segment +=  (r -l + 1)
    return count_segment 
print(segments())
               