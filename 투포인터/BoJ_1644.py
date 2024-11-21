import sys

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    for i in range(2, int(n**(1/2))+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

input = sys.stdin.readline
N = int(input())

prime = prime_numbers(N)

left, right, count = 0, 0, 0

while right < len(prime):
    total = sum(prime[left:right+1])
    if total > N:
        left += 1
    elif total < N:
        right += 1
    else:
        count += 1
        right += 1
print(count)


