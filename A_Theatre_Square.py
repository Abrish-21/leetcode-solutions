import math 
def time_square():
    l,w,n = map(int, input().split())

    return math.ceil(l / n) * math.ceil(w / n)
print(time_square())