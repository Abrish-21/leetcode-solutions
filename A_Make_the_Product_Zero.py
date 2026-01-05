import math
def makeZero():
    t = int(input())
    arr= list(map(int, input().split()))
    for i in range(t):
        arr[i] = abs(arr[i])
    return min(arr)
print(makeZero())
