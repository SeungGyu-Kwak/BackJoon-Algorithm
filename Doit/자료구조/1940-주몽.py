# 주몽
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())
ary = list(map(int, input().split()))
i = 0
j = len(ary)-1
ary.sort() # 오름차순으로 정렬
sum = 0
count = 0
while i < j:
  sum = ary[i] + ary[j]
  if sum == M:
    count += 1
    i += 1
    j -= 1
  elif sum < M:
    i += 1
  elif sum > M:
    j -= 1
print(count)