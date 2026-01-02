from collections import defaultdict 
n = int(input())

r = list(map(int, input().split()))
c = list(map(int, input().split()))

c.sort(reverse  = True)
two_coca = sum(c[:2])

if two_coca >= sum(r):
    print('YES')
else:
    print('NO')



