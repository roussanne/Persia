t = int(input())

for tc in range(1, 1+t):
    n,m = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    if n > m:                              # a의 갯수와 n값이 항상 작도록
        n, m = m, n                        # 길이 바꿈
        a, b = b, a                        # 숫자열 바꿈

    mov = m-n + 1                          # 움직일 수 있는 범위
    maxi = -float('inf')                   # 최댓값 저장

    for j in range(mov):                   # 움직이는 거리
        c = 0                              # 더한 값 저장 변수 선언
        for k in range(n):                 # 작은 list 크기만큼
            c += b[j+k] * a[k]             # 마주보는 두 수 곱해서 더함

        maxi = max(maxi, c)                # 더 큰값 저장
 
    print(f"#{tc} {maxi}")