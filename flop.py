20397

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for _ in range(m):
        i, j = map(int, input().split())
        i -= 1
        
        for k in range(1, j+1):
            left = i - k
            right = i + k
            
            if left < 0 or right >= n:
                break
            
            if arr[left] == arr[right]:
                arr[left] = 1 - arr[left]
                arr[right] = 1 - arr[right]
    
    
    print(f"#{tc}", *arr)






# 3              testcase

# 5 1            n,m

# 0 1 0 1 0      n개 초기상태
# 2 2            ij

# 5 1           

# 0 1 0 0 0
# 2 3


# 10 4

# 0 1 1 0 0 1 0 1 0 1
# 3 2
# 5 3
# 4 4
# 8 4


#1 1 1 1 1 0
#2 1 1 1 0 0
#3 1 0 0 0 0 0 1 0 1 0