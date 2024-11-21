import math

# 자릿수의 합을 구하는 함수 123 => 6
def get_jarisu(n):
    return sum(map(int, str(n)))

# 소수 인지
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 최대 공약수
def get_gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# 입력
N = int(input())
Array = list(map(int, input().split()))

prime = []

# 각 숫자의 자릿수 합이 소수인 숫자를 찾기
for num in Array:
    if is_prime(get_jarisu(num)):
        prime.append(num)

# 자릿수 합이 소수인 숫자가 2개 미만인 경우 -1 출력
if len(prime) < 2:
    print(-1)
else:
    max_gcd = 0
    # GCD중 최대값만 출력
    for i in range(len(prime)):
        for j in range(i + 1, len(prime)):
            max_gcd = max(max_gcd, get_gcd(prime[i], prime[j]))
    print(max_gcd)


# 숫자들의 비밀
# 어느 날, 너는 마법의 숫자 세계에 발을 들였어. 이곳의 숫자들은 각자 자신만의 비밀을 가지고 있고,
# 그 비밀을 풀어야 최대 공약수라는 강력한 힘을 얻을 수 있어. 하지만 그 비밀은 간단한 게 아니야. 
# 숫자들은 특정 조건을 만족해야만 그들의 최대 공약수를 계산할 수 있거든.

# 입력
# 숫자 세계의 주인으로서, 먼저 숫자들의 수를 정해야 해. 첫 번째 줄에 정수 N (1 ≤ N ≤ 104)을 입력받아. 
# 이건 다음에 입력될 숫자의 개수를 나타내.

# 그 후, 두 번째 줄부터 N개의 정수가 주어져. 각 정수는 1 ≤ A[i] ≤ 104의 범위를 가져. 
# 숫자들은 다양한 비밀을 가지고 있으니까, 자릿수의 합을 사용해서 풀어내야 해.

# 출력
# 숫자들의 비밀을 풀어내고, 자릿수의 합이 소수인 숫자들 중에서 최대 GCD를 찾아야 해
# (즉, 자릿수의 합이 소수인 숫자 쌍 끼리의 GCD 중 제일 큰 값을 찾아야 해). 
# 만약 조건을 만족하는 숫자가 두 개 미만이라면, 그 비밀을 풀 수 없다는 뜻으로 -1을 출력해.

# 세부사항
# 자릿수의 합: 각 숫자의 자릿수의 합을 계산해야 해. 예를 들어, 숫자 123의 자릿수의 합은 1 + 2 + 3 = 6이야.
# 소수 판별: 자릿수의 합이 소수인지 확인해야 해. 소수는 1과 자기 자신만을 약수로 가지는 자연수야. 
# 예를 들어, 2, 3, 5, 7 등이 소수야.
# GCD 계산: 조건을 만족하는 숫자들 간의 최대 공약수를 계산해. 
# 최대 공약수는 주어진 숫자 집합에서 공통적으로 나누어 떨어지는 가장 큰 숫자야.
# 이제 너의 지혜를 발휘해서 이 숫자들의 비밀을 밝혀내고, 최대 공약수라는 강력한 힘을 손에 넣어봐!

# For example:

# Input	
# 5
# 12 13 15 20 30

# Result
# 10


# Input	
# 4
# 7 8 10 14

# Result
# 7


# Input	
# 3
# 29 37 41

# Result
# 1
