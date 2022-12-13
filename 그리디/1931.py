# 회의실 배정

import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
time = [[0]*2 for _ in range(N)]
for i in range(N):
  start, end = map(int, sys.stdin.readline().split())
  time[i][0] = start
  time[i][1] = end

# 끝나는 시간을 가지고 오름차순으로 정렬 후, 시작 시간을 가지고 정렬해줌
time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)