import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

A = deque()

for i in range(N):
    string = input().split()
    if string[0] == "push":
        A.append(int(string[1]))
    elif string[0] == "pop":
        if A:
            ch = A.popleft()
            print(ch)
        else:
            print(-1)
    elif string[0] == "size":
        print(len(A))
    elif string[0] == "empty":
        if A:
            print(0)
        else:
            print(1)
    elif string[0] == "front":
        if A:
            print(A[0])
        else:
            print(-1)
    elif string[0] == "back":
        if A:
            print(A[-1])
        else:
            print(-1)
