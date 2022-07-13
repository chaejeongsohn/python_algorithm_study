
#input은 입력되는 모든 것을 문자열로 취급함
#문자열 띄어쓰기는 콤마로 한다

#input().split()의 결과는 문자열 리스트 ==[~,~]
#map을 사용해서 정수로 변환

A, B = map(int,input().split())
if A>B:
    print(">")
elif A<B:
    print("<")
elif A==B:
    print("==")

#시험성적
#int(input()) 이용해서 타입 바꿔주기
#A = input()
A=int(input())
if A<=100 and A>=90:
    print("A")
elif A<90 and A>=80:
    print("B")
elif A<80 and A>=70:
    print("C")
elif A<70 and A>=60:
    print("D")
else: 
    print("F")

#사분면
#A, B = map(int,input().split("\n"))
A = int(input())
B = int(input())
if A>0 and B>0:
    print(1)
elif A<0 and B>0:
    print(2)
elif A<0 and B<0:
    print(3)
elif A>0 and B<0:
    print(4)

#윤년


