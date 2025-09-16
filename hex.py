# 16진수의합

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    hexe = str(input())
    some = 0
    arr = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

    for i in range(n):
        a = hexe[i]

        if '0' <= a <= '9':
            some += int(a)
        
        else:
            some += arr[a]
        
    print(f'#{tc} {some}')