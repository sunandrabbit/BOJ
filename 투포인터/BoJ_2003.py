import sys
input=sys.stdin.readline
 
N,M=map(int, input().split())
A=list(map(int, input().split()))
start_index = 0
end_index = 1
count = 0
 
while start_index <= end_index and end_index <= N:
    total=sum(A[start_index:end_index])

    if total < M: 
        end_index += 1
    elif total > M:
        start_index += 1
    else:
        count += 1
        end_index += 1
 
print(count)