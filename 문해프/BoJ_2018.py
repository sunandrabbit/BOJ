number = int(input())

start = 1
end = 1
sum = 1
count = 1
    
while end != number:
    if sum == number:
        count += 1
        end += 1
        sum += end
    if sum < number:
        end += 1
        sum += end
    if sum > number:
        sum -= start
        start += 1
print(count)