#단어개수
i = input().split()
print(len(i))

#단어공부
# count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수
word = input()
word = word.upper()
w_list = list(set(word))
result=[]
for i in range(len(w_list)):
    result.append(list(word).count(w_list[i]))
M = max(result)
if result.count(M) != 1:
    print("?")
else:
    print(w_list[result.index(M)])

##단어공부-풀이2
#왼쪽 공백 지우기(lstrip)
#오른쪽 공백 지우기(rstrip)
#양쪽 공백 지우기(strip)
word= list(sys.stdin.readline().rstrip().upper())
check = list(set(word))
result=[]
for i in check:
    result.append(word.count(i))


#평균
n = int(input()) #과목수
t_list = list(map(int, input().split()))
max_score = max(t_list)
new_list =[]
for s in t_list:
    new_list.append(s/max_score*100)
A= sum(new_list)/n
print(A)

##평균-풀이2
n = int(input()) #과목수
score = list(map(int, input().split()))
max_score = max(score)
avg = ((sum(score)/max_score*100)/n)
print(avg)

#별찍기-2
#range(시작 숫자, 끝 숫자) 형태를 사용
#이때 끝 숫자는 포함되지 않는다.
num = int(input())
for i in range(1, num+1):
    print(" "*(num-i)+"*"*i)
    

#검증수
num = list(map(int, input().split()))
num_sum=0
for n in num:
    num_sum+= n**2
print(num_sum%10)

#최댓값
#문자열 띄어쓰기는 콤마로 한다
num = []
for i in range(9):
    num.append(int(input()))
num_max = max(num)
num_index= num.index(num_max)+1
print(num_max)
print(num_index)

#숫자의개수
# num = 0
# for i in range(3):
#     num*=int(input())
# sum = list(str(num).split(""))
# n_list=[]
a= int(input())
b= int(input())
c= int(input())
result = list(str(a*b*c))
for i in range(10):
#     n_list[i]=sum.count(i)
    print(result.count(str(i)))

# print(n_list)


#sys.stdin.readline() = input()
import sys
num = sys.stdin.readline().split()

#숙제 1264, 2440, 2845,3046 (목요일까지)
#코드업 6009~6018 (화요일까지)





#알람시계

#상수

#음계

#나머지

#OX퀴즈

#최소,최대

#숫자의합