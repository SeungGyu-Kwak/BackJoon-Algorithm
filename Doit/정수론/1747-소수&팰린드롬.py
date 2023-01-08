# 소수 & 팰린드롬
import sys
import math
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
A = [0] * (10000001)

# A 리스트 초기화
for i in range(2, len(A)):
  A[i] = i

# 에라토스테네스의 체 사용하여 소수 구하기
for i in range(2, int(math.sqrt(len(A))+1)):
  if A[i] == 0:
    continue
  for j in range(i+i, len(A), i):
    A[j] = 0

# 팰린드롬 판별 함수 구현
def isPalindrome(target):
  temp = list(str(target))
  s = 0
  e = len(temp) - 1
  while s < e:
    if temp[s] != temp[e]:
      return False
    s += 1
    e -= 1
  return True

i = N
while True:
  if A[i] != 0:
    result = A[i]
    if (isPalindrome(result)):
      print(result)
      break
  i += 1
