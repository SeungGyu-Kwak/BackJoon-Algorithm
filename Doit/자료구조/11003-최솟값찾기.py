# 최솟값 찾기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
mydeque = deque() # 덱 자료구조 가지고오기

# 새로운 값이 들어올 때 마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거
for i in range(N):
    while mydeque and mydeque[-1][0] > A[i]:
        mydeque.pop()
    mydeque.append((A[i], i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    
    print(mydeque[0][0], end= " ")


