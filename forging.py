t = int(input())  # 테스트 케이스 개수 입력

for t in range(1, 1 + t):
    n = int(input())  # 수열의 길이
    arr = list(map(int, input().split()))  # 수열 입력

    maxi = -1  # 단조 증가 수의 최댓값 (없으면 -1)

    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]  # 두 수의 곱 계산
            productt = str(product)  # 곱한 수를 문자열로 변환

            # 단조 증가 수 판별
            if all(productt[k] <= productt[k + 1] for k in range(len(productt) - 1)):
                maxi = max(maxi, product)  # 최댓값 갱신

    print(f"#{t} {maxi}")