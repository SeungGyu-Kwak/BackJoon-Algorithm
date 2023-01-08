# 기타레슨
# 순서가 뒤바뀌면안된다, 블루레이는 모두 같은 크기여야 한다.
# 이를 통해 이진탐색 알고리즘을 선택하게 하는 실마리임

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split()) # 강의 수, 블루레이 수
A = list(map(int, input().split())) # 강의 순서대로 담김
# start = A[-1] # 시작인덱스 : 레슨시간 중 가장 긴 값
# end = sum(A) # 종료인덱스 : 레슨시간 다 더한 값
start = 0
end = 0

for i in A:
  if start < i:
    start = i
  end += i

while start <= end:
  mediValue = int((start + end) / 2) # 중앙 값
  sum = 0
  count = 0
  for i in range(N):
    if sum + A[i] > mediValue:
      count += 1
      sum = 0
    sum += A[i]
  if sum != 0: # sum이 0이 아니면 마지막 블루레이가 필요하므로 count값 올리기
    count += 1
  if count > M: # count가 M보다 크면 start값 올려서 다시 하기
    start = mediValue + 1
  else:
    end = mediValue - 1
print(start)
