#16910. 원 안의 점

t = int(input())

for tc in range(1, t + 1):
    r = int(input())

    cnt = 0

    for x in range(-r, r + 1):          # horizontal square grid length
        for y in range(-r, r + 1):      # vertical square grid length
            
            if x **2 + y **2 <= r**2:   # if square grid point is in sqare of the radius of circle
                cnt += 1
                
    print(f"#{tc} {cnt}")
