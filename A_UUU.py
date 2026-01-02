from collections import defaultdict
def work():
    i, jb = map(int, input().split())
    jobs = list(map(int, input().split()))
    time = list(map(int, input().split()))
    pair = []
    time_store = defaultdict(int)
    for i in range(i):
        pair.append((jobs[i], time[i]))

    pair.sort(reverse = True, key = lambda x: x[1])
    remove = []
    for i,j in pair:
        if i not in time_store:
            time_store[i] = j
        else:
            remove.append(j)
    
    remove.sort()
    print(sum(remove[: jb - len(set(jobs))]))
   


work()