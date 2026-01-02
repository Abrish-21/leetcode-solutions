from collections import defaultdict
def uniqueSegment():
    m,k = map(int, input().split())

    arr= list(map(int,input().split()))
    l = 0
    count_segment = 0
    freq_map = defaultdict(int)
    
    
    for r in range(m):
        freq_map[arr[r]] += 1

        while len(freq_map) > k:
            freq_map[arr[l]] -=  1
            if freq_map[arr[l]] == 0:
                del freq_map[arr[l]]
            l += 1
        count_segment += r - l + 1

        

    return count_segment



print(uniqueSegment())

         
