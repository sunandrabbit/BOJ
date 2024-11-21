import sys
import heapq
input = sys.stdin.readline

T = int(input())

for i in range(T):
    
    min_que = []
    max_que = []
    
    N = int(input())

    for j in range(N):
        command, number = input().split()
        number = int(number)
        if command == "I":
            heapq.heappush(min_que, number)
            heapq.heappush(max_que, -number)
            print("min :{}".format(min_que))
            print("max :{}".format(max_que))
        elif command == "D":
            if number == -1:
                if min_que:
                    heapq.heappop(min_que)
                    print("min :{}".format(min_que))
            elif number == 1:
                if max_que:
                    heapq.heappop(max_que)
                    print("max :{}".format(max_que))

    print("min :{}".format(min_que))
    print("max :{}".format(max_que))
    # if que:
    #     min = heapq.heappop(que)
    #     max = heapq._heappop_max(que)
    #     print("{} {}".format(max,min))
    # else:
    #     print("EMPTY")
        
