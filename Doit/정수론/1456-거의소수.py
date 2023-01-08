# 거의 소수
# 소수를 구할 때는 에라토스테네스의 체를 사용함
import sys
import math
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

min, max = map(int, input().split())
A = [0] * (10000001)

# A 리스트 초기화
for i in range(2, len(A)):
  A[i] = i
# 에라토스테네스의 체를 활용하여 소수 구하기
for i in range(2, int(math.sqrt(len(A))+1)):
  if A[i] == 0:
    continue
  for j in range(i + i, len(A), i):
    A[j] = 0
count = 0

for i in range(2, 10000001):
  if A[i] != 0:
    temp = A[i]
    while A[i] <= max / temp:
      if A[i] >= min / temp:
        count += 1
      temp = temp * A[i]
print(count)