#input은 입력되는 모든 것을 문자열로 취급함
#문자열 띄어쓰기는 콤마로 한다

A, B = input().split()
print(int(A)+int(B))
print(int(A)-int(B))
print(int(A)*int(B))
print(int(A)/int(B))
print(int(A)//int(B))
print(int(A)%int(B))

A, B, C = input().split()
print(int(A)+int(B)+int(C))