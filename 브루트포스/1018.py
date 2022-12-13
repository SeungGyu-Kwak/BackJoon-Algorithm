# 체스판 다시 칠하기
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
ary = []
count = []

for _ in range(N):
  ary.append(input())

for i in range(N-7):
  for j in range(M-7):
    count1 = 0
    count2 = 0

    for a in range(i, i+8):
      for b in range(j, j+8):
        if (a + b) % 2 == 0:
          if ary[a][b] != 'W':
            count1 += 1
          if ary[a][b] != 'B':
            count2 += 1
        else:
          if ary[a][b] != 'B':
            count1 += 1
          if ary[a][b] != 'W':
            count2 += 1
    count.append(min(count1, count2))

print(min(count))
