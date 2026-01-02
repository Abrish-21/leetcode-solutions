from collections import defaultdict

def targetSum(arr, target):
    count  = 0
    c = []
    d = []
    l,r = 0 , len(arr) -1

    arr.sort()
    while l< r:
        if arr[l] + arr[r] < target:
            l += 1
        elif arr[l] + arr[r] > target:
            r -= 1
        else:
            count += 1
            c.append(arr[l])
            d.append(arr[r])

            l += 1
            r -= 1
    return count, c, d

t = int(input())
for _ in range(t):
    n, target = map(int, input().split())
    arr = list(map(int,input().split()))
    print(targetSum(arr, target))


    



