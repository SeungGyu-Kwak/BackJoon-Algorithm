import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

MaxValue = -1
num = 0 # 기차에 타고 있는 사람
for i in range(10):
    OUT, IN = map(int, input().split())
    num -= OUT
    num += IN
    
    if MaxValue < num:
        MaxValue = num

print(MaxValue)