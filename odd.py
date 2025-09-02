t = int(input())

for i in range(1, 1+t):
    arr = list(map(int,input().split()))

    odd = 0
    for j in range(10):
        if arr[j] % 2 == 0:
            continue
        
        else:
            odd = odd + arr[j]


    print(f"#{i} {odd}")