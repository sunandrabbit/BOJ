import sys
input = sys.stdin.readline

N = int(input())
A=list(map(int, input().split()))
M = int(input())

A.sort()

left = 0
right = N-1
count = 0

while left < right:
    sum = A[left] + A[right]
    if sum < M:
        left += 1
    elif sum > M:
        right -= 1
    else:
        count += 1
        right -= 1
print(count)
