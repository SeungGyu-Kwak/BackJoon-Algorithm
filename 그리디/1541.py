# 잃어버린 괄호
import sys
sys.stdin = open('input.txt', 'r')

S = input().split('-')
print(S)
result = 0
for i in S[0].split('+'):
  result += int(i)

for i in S[1:]:
  for j in i.split('+'):
    result -= int(j)

print(result)
