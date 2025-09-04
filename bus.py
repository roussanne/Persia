t = int(input())

for tc in range(1, 1 + t):
    k, n, m = map(int, input().split())
    chargers = list(map(int, input().split()))
    
    stops = [0] + chargers + [n]  # 출발점과 도착점 추가
    curr_idx = 0                  # 현재 위치 인덱스
    charges = 0                    # 충전 횟수

    # 불가능 여부 확인
    impossible = any(stops[i+1] - stops[i] > k for i in range(len(stops)-1))
    if impossible:
        print(f"#{tc} 0")
        continue

    while curr_idx < len(stops) - 1:
        next_idx = curr_idx
        # K 범위 안에서 가장 먼 곳으로 이동
        while next_idx + 1 < len(stops) and stops[next_idx + 1] - stops[curr_idx] <= k:
            next_idx += 1

        if next_idx == curr_idx:  # 이동 불가
            charges = 0
            break

        if next_idx == len(stops) - 1:  # 도착점 도달
            curr_idx = next_idx
            break

        charges += 1
        curr_idx = next_idx

    print(f"#{tc} {charges}")