N = int(input())
N_LIST = list(map(int, input().split()))
M = int(input())
M_LIST = list(map(int, input().split()))

N_LIST.sort()

result = []

N_DICT = {}
for n in N_LIST:
  if n in N_DICT:
    N_DICT[n] += 1
  else:
    N_DICT[n] = 1

low, high = 0, M-1

for i in range(M):
    find = M_LIST
    while low < high:
        mid = (low + high)//2
        if N_DICT[mid] == find:
            result.append()