# 균형 잡힌 세상 

import sys
sys.stdin = open('input.txt', 'r')

while True:
  S = input()
  if S == '.':
    break
  stack = []
  temp = True
  for i in S:
    if i == '(' or i == '[':
      stack.append(i)
    elif i == ')':
      if not stack or stack[-1] == '[':
        temp = False
        break
      elif stack[-1] == '(':
        stack.pop()
    elif i == ']':
      if not stack or stack[-1] == '(':
        temp = False
        break
      elif stack[-1] == '[':
        stack.pop()
  if temp == True and not stack:
    print('yes')
  else:
    print('no')