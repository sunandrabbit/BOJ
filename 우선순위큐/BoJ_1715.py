import sys
import heapq
input = sys.stdin.readline

N = int(input())

que = []
for i in range(N):
    heapq.heappush(que, int(input()))

sum = 0

while True:
    if len(que) == 1:
        break
    a = heapq.heappop(que)
    b = heapq.heappop(que)
    sum += a + b

    heapq.heappush(que, a+b)

print(sum)
