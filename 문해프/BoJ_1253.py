n = input()
a = sorted(list(map(int, input().split())))


c = 0

for i in range(n):
    target = a[i]
    start = 0
    end = n-1

    if start == i:
        start += 1
        continue
    if end == i:
        end -= 1
        continue
    
    total = a[start] + a[end]

    while start < end:
        if a[start] + a[end] < target:
            start += 1
        elif a[start] + a[end] > target:
            end -= 1
        else:
            c += 1