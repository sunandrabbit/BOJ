from collections import deque

N = int(input())

que = deque()

for i in range(1,N+1):
    que.append(i)

while True:
    if len(que) == 1:
        break
    que.popleft()
    new = que.popleft()
    que.append(new)

print(que.pop())