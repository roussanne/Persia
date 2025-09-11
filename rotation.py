# 1961. 숫자 배열 회전


t = int(input())
for tc in range(1, 1 + t):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr_90 = [[0] * n for _ in range(n)]        
    arr_180 = [[0] * n for _ in range(n)]
    arr_270 = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            arr_90[j][n - 1 - i] = arr[i][j]                 # i, j change = row columb change, n - 1 - i = i reversing columb 
            arr_180[n - 1 - i][n - 1 - j] = arr[i][j]        # reversing i, reversing j 
            arr_270[n - 1 - j][i] = arr[i][j]                # row columb change, reversing j

    print(f"#{tc}")
    for i in range(n):
        print(''.join(map(str, arr_90[i])), 
            ''.join(map(str, arr_180[i])), 
            ''.join(map(str, arr_270[i])))