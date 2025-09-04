t = int(input().strip())

for tc in range(1, 1 + t):

    n = int(input().strip())
    arr = list(map(int, input().split()))

    max_cnt = 1   # 최소 길이
    cnt = 1       # 연속 증가 길이

    for i in range(1, n):

        if arr[i] > arr[i-1]:   # 증가하는 경우
            cnt += 1

            if cnt > max_cnt:   # 최대값 갱신
                max_cnt = cnt

        else:                   # 증가가 끊기면  reset
            cnt = 1

    print(f"#{tc} {max_cnt}")