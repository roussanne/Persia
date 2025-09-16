# 20739. 고대 유적 2

# 9489. 고대 유적

t = int(input())

for tc in range(1, 1 + t):

    n, m = map(int,input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    
    maxi = 0
    for i in range(n):
        cnt = 0
        for j in range(m):

            if arr[i][j] == 1:
                cnt += 1
                maxi = max(cnt, maxi)

            else:
                cnt = 0


    for j in range(m):
        cnt = 0
        for i in range(n):

            if arr[i][j] == 1:
                cnt += 1
                maxi = max(cnt, maxi)

            else:
                cnt = 0

    
    if maxi == 1:  # added, if maxi is 1 
        maxi = 0   # maxi value is invalid


    print(f'#{tc} {maxi}')
