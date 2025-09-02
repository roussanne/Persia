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

    for j in range(mov):
        c = 0
        for k in range(n):
            c += b[j+k] * a[k]

        maxi = max(maxi, c)
 
    print(f"#{tc} {maxi}")