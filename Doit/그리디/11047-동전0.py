# 동전 0
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split()) # 동전개수, 금액

money = []
for i in range(N):
  money.append(int(input()))

count = 0
for i in range(N-1, -1, -1):
  if money[i] <= K:
    count += int(K / money[i])
    K = K % money[i]

print(count)
