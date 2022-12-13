# 영화감독 숌

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
num = 666
cnt = 0
while True:
  if '666' in str(num):
    cnt += 1
  if cnt == N:
    print(num)
    break
  num += 1
