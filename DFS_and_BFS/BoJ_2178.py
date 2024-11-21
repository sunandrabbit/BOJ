import sys
from collections import deque

def bfs(x, y):
    que = deque()
    que.append((x,y))

    while que:
        x, y = que.popleft() #시작은 0,0

        for i in range(4): # (1,0) (-1,0) (0,1) (0,-1) 네가지 방향을 전부 조사
            nx, ny = x + dx[i], y + dy[i] # 한 방향으로 이동했을 때의 좌표 nx, ny

            if nx < 0 or ny < 0 or nx >= N or ny >= M: # 0~N-1 , 0~M-1 사이의 값인지 아니면 다음 for문
                continue

            if maze[nx][ny] == 0: # 0은 벽이므로 다음 for문
                continue

            if maze[nx][ny] == 1: # 1은 갈수 있는 칸이므로
                maze[nx][ny] = maze[x][y] + 1 # 이동 전 좌표의 (거리) + 1
                
                print("maze :")
                for i in range(N):
                    print(maze[i])
                

                que.append((nx, ny)) # 이동한 좌표를 큐에 넣음

    return maze[N-1][M-1]

input = sys.stdin.readline

N,M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maze = []
for _ in range(N):
    maze.append(list(map(int, str(input().strip()))))

print(bfs(0,0))

