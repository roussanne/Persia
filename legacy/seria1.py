t = int(input().strip())

for tc in range(1, 1 + t):

    n = input()
    arr = input().strip()

    maxcnt = 0                 # 연속 1의 최대 개수
    cnt = 0                    # 현재 연속 1의 개수

    for ch in arr:
        
        if ch == '1':          # 1이면 카운트 ++
            cnt += 1

            if cnt > maxcnt:
                maxcnt = cnt
        else:                  # 0이면 reset
            cnt = 0

    print(f"#{tc} {maxcnt}")
