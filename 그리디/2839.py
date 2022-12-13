# 설탕 배달

N = int(input())

count = 0
count = N // 5
N = N % 5

while True:
  if count < 0:
    break
  if N % 3 == 0:
    tmp = N // 3
    count = count + tmp
    break
  else:
    count -= 1
    N = N + 5
print(count)
