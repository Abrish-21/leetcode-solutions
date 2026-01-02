vid, post = map(int, input().split())
video = list(map(int, input().split()))

total = 0
count = 0
result = []
total_duration = sum(video)
target = total_duration / post
for v in video:
    total += v
    count += 1
    if total == target:
        result.append(str(count))
        count = 0
        total = 0
if len(result) == post:
    print('Yes')
    print(' '.join(result))
else:
    print('No')
