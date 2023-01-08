# 회의실 배정
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 회의 수
A = [[0] * 2 for _ in range(N)]

for i in range(N):
  S, E = map(int, input().split())
  A[i][0] = E # 종료시각 우선 정렬이 먼저이므로 0번째에 종료 시각 먼저 저장
  A[i][1] = S

A.sort()
count = 0
end = -1

for i in range(N):
  if A[i][1] >= end: # 겹치지 않는 다음 회의가나온 경우
    end = A[i][0]
    count += 1
print(count)