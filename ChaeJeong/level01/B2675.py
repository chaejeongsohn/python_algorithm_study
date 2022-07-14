#문자열 반복
import sys

n= int(input())

for i in range(n):
    num, code = input().split()
    for j in range(len(code)):
        print(code[j]*int(num), end='')
    print()
