# 퇴사
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 남은 N일
T = [0] * (N+1) # 상담을 완료하는데 걸리는 기간 리스트
P = [0] * (N+1) # 상담을 했을 때 받을 수 있는 금액 리스트

# 값 받기
for i in range(1, N+1):
  T[i], P[i] = map(int, input().split())

D = [0] * (N+2) # DP테이블 생성
for i in range(N, 0, -1):
  if i + T[i] > N+1: # 기간을 초과하면
    D[i] = D[i+1]
  else:
    D[i] = max(D[i+1], D[i+T[i]] + P[i])

print(D[1])
