# 수 찾기
# 이진탐색을 활용하여 문제를 해결
# 이진탐색을 하기 위해서는 데이터가 정렬되어 있어야 함

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 자연수 개수
A = list(map(int, input().split()))
A.sort() # 정렬하기
num = int(input()) # 찾아야 할 수
target_list = list(map(int, input().split()))

for i in range(N):
  find = False
  target = target_list[i]
  # 이진 탐색
  start = 0
  end = len(A)-1
  while start <= end:
    mid = int((start+end)/2)
    midValue = A[mid]
    if midValue > target:
      end = mid - 1
    elif midValue < target:
      start = mid + 1
    else:
      find = True
      break
  if find:
    print(1)
  else:
    print(0)
