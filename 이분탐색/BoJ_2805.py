import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

low, high = 0, max(A)
answer = 0

while low <= high:
    wood = 0
    mid = (low + high)//2

    for height in A:
        if height > mid:
            wood += height - mid 
    
    if wood >= M:
        answer = mid
        low = mid + 1 
    else:
        high = mid - 1 

print(answer)