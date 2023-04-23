# 수 찾기
# 이진탐색을 활용하여 문제를 해결
# 이진탐색을 하기 위해서는 데이터가 정렬되어 있어야 함

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
findList = list(map(int, input().split()))

# 이진탐색을 위해 정렬 
A.sort()

for i in range(M):
    find = False
    target = findList[i]
    
    #이진탐색시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    
    if find:
        print(1)
    else:
        print(0)