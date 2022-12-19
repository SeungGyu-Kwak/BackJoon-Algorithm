# 소트인사이드

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

ary = list(input())
ary.sort(reverse = True)
result = ''
for i in range(len(ary)):
  result += ary[i]
print(int(result))       