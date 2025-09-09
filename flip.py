t = int(input())

for tc in range(1, 1+t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for _ in range(m):
        i, j = map(int, input().split())
        colour = arr[i-1]                 # i번째 돌 포함 색깔
        for k in range(j):                # j번 반복
            if i-1 + k < n:               # i번째 돌 포함 + k가 n보다 작아야 range 유지
                arr[i-1+k] = colour       # i번째 돌부터  j번까지 색칠

    print(f"#{tc}", *arr)





# 3         테스트케이스

# 5 1                         5개 배치 테스트케이스 1회
# 0 1 0 1 0                   초기상태
# 2 2                         2번째 2개 뒤집음

# 5 1                         5개 배치 테스트케이스 1회
# 0 1 0 0 0                   초기상태
# 2 3                         2번째 3개 뒤집음

# 10 4                        10개 배치 테스트 케이스 4회
# 0 1 1 0 0 1 0 1 0 1    10   초기상태
# 3 2                         3번째 2개 뒤집음
# 5 3                         5번째 3개 뒤집음
# 4 4                         4번째 4개 뒤집음
# 8 4                         8번째 4개 뒤집음