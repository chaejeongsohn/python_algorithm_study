#문자열 띄어쓰기는 콤마로 한다
#문자열에서 +는 붙여쓴다
H, M = input().split()
H=int(H)
M=int(M)
if M<45:
    M=60-(45-M)
    if H==0:
        H=23
    else: H-=1
elif M>=45:
    M-=45
print(H,M)


#오답(반례: 0 45)
# if H==0: H=24
# if M<45: 
#     H-=1
#     M=60-(45-M)
# elif M==45:
#     H-=1
#     M=0
# else:
#     M-=45
# if H==24: H=0

