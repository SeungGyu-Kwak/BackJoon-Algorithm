# 배열에서 K번째 수 찾기
# 이분탐색으로 풀면된다 -> 이렇게 알고리즘을 찾는게 어려움

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
K = int(input())
ans = 0
start, end = 1, K
while start <= end:
  mid = (start + end) // 2
  cnt = 0
  for i in range(1, N+1):
    cnt += min(int(mid / i), N)
  if cnt < K:
    start = mid + 1
  else:
    ans = mid
    end = mid - 1
print(ans)