#map()은 반복 가능한 객체(리스트 등)에 대해
#각각의 요소들을 지정된 함수로 처리해주는 함수입니다.

n, area = input().split()
target = list(map(int, input().split()))
for t in target:
    print(t-(int(n)*int(area)), end=' ')