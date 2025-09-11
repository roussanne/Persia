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




t = int(input())

for tc in range(1, 1+t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    maxi = -1  # 단조 증가 수의 최댓값
    
    for i in range(n):
        for j in range(i+1, n):
            product = arr[i] * arr[j]   # 두 수의 곱
            s = str(product)            # 문자열로 변환
            
            # 자리 비교
            for k in range(len(s)-1):
                if s[k] > s[k+1]:       # 앞자리가 뒷자리보다 크면 X
                    break
            
            else:
                maxi = max(maxi, product)
    
    print(f"#{tc} {maxi}")

# 곱한값을 문자열로 받아서 각 자리 비교
# for else로 앞자리 가 뒷자리 크면 break 아니면 갱신




"""
6190

정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.

그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.

어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.

예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.

양의 정수 N 개 A1, …, AN이 주어진다.

1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.





[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.

두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.

1
4
2 4 7 10	// 테스트케이스 개수, T=1
// N=4
// A1=2, A2=4, A3=7, A4=10




[출력]

각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.

만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.

#1 28	//첫 번째 테스트케이스 결과


"""



t = int(input())

for tc in range(1, 1+t):
    n = int(input())
    arr = list(map(int, input().split()))

    maxi = -1

    for i in range(n):
        for j in range(1+i, n):
            c = arr[i] * arr[j]
            s = str(c)

            for k in range(len(s)-1):
                if s[k] > s[k+1]:
                    break
                
                else:
                    maxi = max(maxi, c)
    
    print(f"#{tc} {maxi}")                 


