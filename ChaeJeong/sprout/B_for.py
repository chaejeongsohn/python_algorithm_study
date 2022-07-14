'''순회할 리스트가 정해져 있고,
그 리스트에서 하나씩 꺼내 쓰기만 되는 상황이라면
for in list를,
순회할 횟수가 정해져 있거나
1씩 증가하는 숫자가 필요하다면
for in range()를 사용하는 것이 좋습니다.'''

#enumerate
# 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
rainbow=["빨","주","노","초","파","남","보"]
for i,color in enumerate(rainbow):
    print('{}번째 색은 {}'.format(i+1,color))


days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i, day in enumerate(days):
    print('{}월의 날짜수는 {}일 입니다.'.format(i+1,day))