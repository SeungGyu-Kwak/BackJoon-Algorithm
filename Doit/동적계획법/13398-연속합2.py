import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 왼쪽으로 합배열 구하기
L = [0] * N
L[0] = A[0]
result = L[0]

for i in range(1, N):
    L[i] = max(A[i], L[i-1] + A[i])
    result = max(result, L[i])

# 오른쪽에서 더한 합 배열 구하기
R = [0] * N
R[N-1] = A[N-1]

for i in range(N-2, -1, -1):
    R[i] = max(A[i], R[i+1] + A[i])

# 수열에서 하나의 숫자를 제거하고 난 후의 결과 보기
for i in range(1, N-1):
    temp = L[i-1] + R[i+1]
    result = max(result, temp)
print(result)