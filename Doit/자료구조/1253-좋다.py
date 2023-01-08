# 좋다

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

# ary 정렬하기
ary.sort()
count = 0
for t in range(N):
  find = ary[t] # 찾고자 하는 수
  i = 0 # 시작 포인터
  j = len(ary)-1 # 끝 포인터
  while i < j:
    if ary[i] + ary[j] == find:
      if i != t and j != t:
        count += 1
        break
      elif i == t:
        i += 1
      elif j == t:
        j -= 1
    elif ary[i] + ary[j] > find:
      j -= 1
    else:
      i += 1

print(count)


