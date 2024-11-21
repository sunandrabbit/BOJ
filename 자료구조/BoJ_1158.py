import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

A = [i for i in range(1,N+1)]
S = []

que = deque(A)

i = 1
while que:
    if i % M == 0:
        b = que.popleft()
        S.append(b)
        i += 1
    else:
        a = que.popleft()
        que.append(a)
        i += 1

print("<", end="")
for i in range(len(S)-1):
  print(S[i], end=", ")
print(str(S[len(S)-1])+">")
