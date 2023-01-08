# 최대공약수

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)

temp = gcd(a, b)
for i in range(temp):
  print('1', end = '')
