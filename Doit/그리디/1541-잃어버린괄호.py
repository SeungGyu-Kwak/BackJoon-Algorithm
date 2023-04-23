# 잃어버린 괄호
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

listA = list(map(str,input().split("-")))
#print(listA)

def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

answer = 0
for i in range(len(listA)):
    temp = mySum(listA[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)
