import heapq

N = int(input())
Array = []
for i in range(N):
    priority, arrival, heal = map(int, input().split())
    Array.append((priority, arrival, heal, i)) # 손님 순서대로 뽑아야 되서 i 요소 추가

Array.sort(key=lambda x : x[1]) # 문제의 함정, 도착 시간 순서대로 받으며, 우선순위를 따져야 했음. 그래서 도착시간 순서대로 정렬
pq = [] # 우선순위 큐
time = 0 # 실제 시각
result = [0]*N # 결과를 담을 배열
i = 0 # 손님 인덱스
while i < N or pq:
    while i < N and Array[i][1] <= time:
        priority, arrival, heal, index = Array[i]
        heapq.heappush(pq, (priority, arrival, index, heal))
        i+=1

    if pq:
        priority, arrival, index, heal = heapq.heappop(pq)
        result[index] = time
        time += heal
    else:
        time = Array[i][1]

print(result)


# 병원 대기열 관리
# 한 병원에서는 환자들을 치료하기 위해 대기열을 관리하고 있습니다. 
# 각 환자는 도착 시각, 치료를 받기 위해 필요한 시간, 그리고 우선 순위를 가지고 있습니다. 
# 우선 순위가 높은 환자가 먼저 치료를 받게 됩니다. 만약 우선 순위가 같다면, 도착 시각이 더 빠른 환자가 먼저 치료를 받습니다.

# 병원에서는 N명의 환자가 대기하고 있으며, 각각의 환자는 다음과 같은 정보를 가지고 있습니다:

# 우선 순위 (값이 작을 수록 우선순위가 높음, 즉 0이 제일 높음)
# 도착 시각
# 치료 필요 시간
 
# 입력:
# 첫 번째 줄에 정수 N (1 ≤ N ≤ 105)이 주어집니다. (N은 대기 중인 환자의 수)
# 두 번째 줄부터 N개의 줄에 걸쳐 각 환자의 우선 순위, 도착 시각, 치료 필요 시간이 주어집니다.

# 출력:
# 치료 시작 시각을 환자 1부터 N까지 순서로 한 줄에 하나씩 출력합니다.

# 제한사항:
# 우선 순위는 0 이상 100 이하의 정수입니다.
# 도착 시각은 0 이상 109 이하의 정수입니다.
# 치료 필요 시간은 1 이상 100 이하의 정수입니다.

#For example:

# Input	      
# 5
# 0 0 3
# 1 1 2
# 0 2 1
# 2 3 1
# 1 4 1
# Output
# 0
# 4
# 3
# 7
# 6   
                  
# Input
# 4
# 2 0 2
# 1 1 1
# 0 2 3
# 0 3 2
# Output
# 0
# 7
# 2
# 5

# Input
# 3
# 1 0 5
# 0 1 2
# 1 3 1
# Output
# 0
# 5
# 7