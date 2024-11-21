import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

list = []

for _ in range(N):
    list.append(int(input()))

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        list[b-1] = c
    else:
        print(sum(list[b-1:c]))