t = int(input())

for i in range(1, t + 1):
    asdf = list(map(int, input().split()))
    v = 0                                       # 합계산 저장 변수선언
    for j in range(10):                         # 10개 수 입력
        v += asdf.pop()                         # pop 전체합
    avg = v / 10                                # 평균계산
    print(f"#{i} {round(avg)}")

