# 주유소
# 현재 도시에서 기름 값을 보고 만약 다음 또는 다음 도시에 기름 값이 더 싼 것이 있으면
# 바로 다음 도시까지 가는 기름 만 넣음. 
import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # 도시 개수
roadLength = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

c = price[0]
result = 0

for i in range(N-1):
  if c >= price[i]:
    c = price[i]
  result += c * roadLength[i]

print(result)