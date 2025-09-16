# # 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용


# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())

#     arr = [list(map(int, input().split())) for _ in range(n)]
#     a = 0
#     b = 0
#     c = 0

#     for i in range(n):
#         for j in range(n):
            






import random

t = int(input())
for tc in range(1, 1+t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    products = list(range(n))
    ans = float('inf')

    K = 10000

    for _ in range(K):
        random.shuffle(products)
        total = 0
    
        for i in range(n):
            total += arr[i][products[i]]
        ans = min(ans, total)

    print(f"#{tc} {ans}") 



    def dfs(i, total):
    global ans
    # 가지치기: 이미 최소비용보다 크면 중단
    if total >= ans:
        return
    
    # 모든 공장에 배정 완료
    if i == n:
        ans = min(ans, total)
        return
    
    # i번 공장에 j번 제품 배정
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            dfs(i+1, total + arr[i][j])
            visited[j] = False



def dfs(i, total):
    global ans
    # 가지치기: 이미 최소비용보다 크면 중단
    if total >= ans:
        return
    
    # 모든 공장에 배정 완료
    if i == n:
        ans = min(ans, total)
        return
    
    # i번 공장에 j번 제품 배정
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            dfs(i+1, total + arr[i][j])
            visited[j] = False


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [False] * n
    ans = float('inf')
    
    dfs(0, 0)
    
    print(f"#{tc} {ans}")