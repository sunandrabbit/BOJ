# 시간 제한	메모리 제한	
# 0.5 초    128 MB	

# 문제
# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 
# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 
# 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
 
# 입력
# 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 
# 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

# 출력
# 첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

# 예제 입력 1 
# 10 15
# 5 1 3 5 10 7 4 9 2 8

# 예제 출력 1 
# 2

N, S = map(int, input().split())
Arr = list(map(int, input().split()))

left = 0
right = 0
sum = 0
result = N + 1

while right < N:
    sum += Arr[right]
    right += 1

    while sum >= S:
        result = min(result, right - left)
        sum -= Arr[left]
        left += 1

if result == N + 1:
    print(0)
else:
    print(result)