# 잃어버린 괄호
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

data = input().split('-')

def mySum(i):
  sum = 0
  temp = str(i).split('+')
  for t in temp:
    sum += int(t)
  return sum

answer = 0

for i in range(len(data)):
  tmp = mySum(data[i])
  if i == 0:
    answer += tmp
  else:
    answer -= tmp
print(answer)