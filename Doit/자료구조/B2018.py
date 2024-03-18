import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
count = 1
start_idx, end_idx = 1, 1
sum = 1

while end_idx != N:
  if sum == N:
    count += 1
    end_idx += 1
    sum += end_idx
  elif sum > N :
    sum -= start_idx
    start_idx += 1
  else:
    end_idx += 1
    sum += end_idx

print(count)
