t = int(input())

for i in range(1, 1+t):
    arr = list(map(int,input().split()))  

    odd = 0                                 # 합계산 저장 변수선언
    for j in range(10):                     # 10개 수 입력
        if arr[j] % 2 == 0:                 # if 짝수 continue
            continue
        
        else:                               # 홀수는 odd에 더함
            odd = odd + arr[j]


    print(f"#{i} {odd}")