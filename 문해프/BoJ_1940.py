n = int(input())
m = int(input())
a = sorted(list(map(int, input().split())))

count = 0
start = 0
end = n-1
while start < end:
    if a[start] + a[end] < m:
        start += 1
    elif a[start] + a[end] == m:
        count += 1
        end -= 1
        start += 1
    else:
        end -= 1
print(count)
