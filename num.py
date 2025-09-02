t = int(input())

for tc in range(1, 1+t):
    n,m = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    if n > m:
        n, m = m, n
        a, b = b, a

    mov = m-n + 1
    maxi = -float('inf')

    for j in range(mov):
        c = 0
        for k in range(n):
            c += b[j+k] * a[k]

        maxi = max(maxi, c)
 
    print(f"#{tc} {maxi}")