T = int(input())

for tc in range(1, T+1):
    origin = list(input())

    n = len(origin)
    mem = ["0"] * n
    cnt = 0

    for i in range(n):

        ith_char = origin[i]

        if ith_char != mem[i]:
            cnt += 1

            for j in range(i, n):
                mem[j] = ith_char

        if mem == origin:
            break

    print(f"#{tc} {cnt}")
