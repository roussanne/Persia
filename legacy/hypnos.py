t = int(input())

for tc in range(1, 1+t):
    N = int(input())
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]       # 찾아야할 숫자 list
    arrr = [int(a) for a in str(N)]            # N번째 본 숫자 list
    brrr = []
    d = 1

    for i in arrr:                             # arrr에 있는 숫자 brrr에 중복없이 stack
        if i not in brrr:
            brrr.append(i)

    brrr.sort()                                # 순서대로 정렬

    while arr != brrr:                         # 찾아야 할 숫자와 N번째 찾은 숫자 비교
        
        arrrr = [int(a) for a in str(N*d)]     # arrrr에 d * N 번쨰 숫자 list 
        for i in arrrr: 
            if i not in brrr:                  # brrr에 arrrr에 값이 없으면 brrr에 추가
                brrr.append(i)
        brrr.sort()                            # brrr 재정렬
        
        d += 1                                 # d++ 해서 반복 
       

    print(f"#{tc} {N*(d-1)}")

# N을  arrr에 자릿수 분리해서 list 생성
# arrr을 stack 사용해서 중복제거 brrr 생성, brrr sort 
# N * d++해서 arrrr list 생성, brrr에 없는 arrrr숫자 brrr에 추가
# arr == brrr 될때까지 반복
