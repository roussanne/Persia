# T = int(input())

# for tc in range(1, T+1):
#     origin = list(input())

#     n = len(origin)
#     mem = ["0"] * n
#     cnt = 0

#     for i in range(n):

#         ith_char = origin[i]

#         if ith_char != mem[i]:
#             cnt += 1

#             for j in range(i, n):
#                 mem[j] = ith_char

#         if mem == origin:
#             break

#     print(f"#{tc} {cnt}")




t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().strip())) # 1자리씩 원래 메모리 값 enlist
    cnt = 0                               # 변경 횟수 카운터
    c = 0                                 # 초기 메모리

    for i in arr:                         # arr의 값 순서대로 i
        if i != c:                        # i가 c와 다르면
            
            c = i                         # c = i c 부호변경 
            cnt += 1                      # 카운트 ++

    print(f"#{tc} {cnt}")