import sys
input = sys.stdin.readline

N = int(input())
N_LIST = set(map(int, input().split()))
M = int(input())
M_LIST = list(map(int, input().split()))

for i in range(M):
    if M_LIST[i] in N_LIST:
        print(1)
    else:
        print(0)
