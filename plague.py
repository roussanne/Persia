t = int(input())

for tc in range(1, 1+t):
    size = int(input())
    asdff=[]                                     # 전체 리스트
    asdf=[]                                      # 행 리스트
    centre = size//2                             # 가운데값
    c = 0                                        # 합계
                                     
    for i in range(size):
        asdf = list(map(int,input()))            # 행 입력
        asdff.append(asdf)                       # 전체 리스트에 추가
        
        dt = abs(centre - i)                     # 중심에서 거리
        for j in range(dt, size - dt):           # 열 만큼 반복
            c += asdff[i][j]

    print(f"#{tc} {c}")

