import sys
input = sys.stdin.readline

# def dfs(start):
#     stack = [start]  # DFS를 위한 스택
#     visited[start] = True
    
#     while stack:
#         node = stack.pop()
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 parent[neighbor] = node  # 부모 노드 설정
#                 stack.append(neighbor)

sys.setrecursionlimit(10**6) # 재귀 방식을 쓰려면 해당 코드 삽입 안쓰려면 위와 같이 스택으로 구현

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            parent[i] = start
            dfs(i)
    

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N+1)
parent = [0]*(N+1)
dfs(1)
for i in range(2,N+1):
    print(parent[i])