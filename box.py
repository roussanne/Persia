5789. 현주의 상자 바꾸기

t = int(input())

for tc in range(1, t + 1):
    n, q = map(int, input().split())        # n box number q number of renewal
    box = [0] * n
    
    for tcc in range(q):
        l , r = map(int, input().split())   # l, r range of number renewal
        
        for i in range(l-1, r):             # renewal 
            box[i] = tcc+1

    print(f"#{tc}", *box) 