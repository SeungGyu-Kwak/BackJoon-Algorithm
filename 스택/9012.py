# 괄호

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 개수 입력받기
N = int(input())
for n in range(N):
  stack = []
  A = input()
  for a in A:
    if a == '(':
      stack.append(a)
    elif a == ')':
      if stack: # 스택에 값이 있으면
        stack.pop()
      else:
        print('NO')
        break
  else: # for-else 문으로 for문에서 한번도 break가 난적이 없으면 else문 실행
    if len(stack) == 0:
      print('YES')
    else:
      print('NO')
    
 
