t = int(input())

for tc in range(1, t + 1):
    n, q = map(int, input().split())
    box = [0] * n
    
    for tcc in range(q):
        l , r = map(int, input().split())
        
        for i in range(l-1, r):
            box[i] = tcc+1

    print(f"#{tc}", *box) 