import sys
input=sys.stdin.readline
 
N,M=map(int, input().split())
A=list(map(int, input().split()))

total = sum(A[:M])
max = total
for i in range(M,N):
    total = total + A[i] - A[i-M]
    if total > max:
        max = total

print(max)