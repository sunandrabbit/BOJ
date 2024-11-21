import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False]*(V+1)
dfs(1)

count = 0

for i in range(V+1):
    if visited[i] == True:
        count += 1

print(count-1)
