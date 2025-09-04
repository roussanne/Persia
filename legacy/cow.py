t = int(input())

for tc in range(1, 1+t):
    N = int(input())
    prime = [2, 3, 5, 7, 11]    # a, b, c, d, e 
    pc = [0] * 5                # 카운트 배열


    def fuc(N):                
        if N == 0:                  # N = 0이면 함수종료
            return

        else:
            for i in range(5):              # prime 값 1개씩 반복
                while N % prime[i] == 0:    # prime 값 나눌 수 있을 만큼 반복
                    N = N // prime[i]       # 값을 나누고 저장
                    pc[i] += 1              # 카운트 배열에 나눈값의 위치에 ++
            return N                        

    fuc(N)
    print(f"#{tc} {' '.join(map(str, pc))}") #list 출력형식에 맞게 변환
