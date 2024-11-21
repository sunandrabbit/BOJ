import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = []

for i in range(N):
    A.append(int(input()))

low, high = 0, max(A)
answer = 0

while low <= high:
    count = 0
    mid = (low+high)//2
    for i in range(N):
        count += A[i]//mid
    
    if count < M:
        high = mid - 1
    elif count >= M:
        low = mid + 1
        if answer < mid:
            answer = mid       

print(answer)

