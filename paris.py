# 6019. 기차 사이의 파리

t = int(input())

for tc in range(1, t + 1):
    d, a, b, f = map(int, input().split()) # d distance, a train A speed , b train B speed, f paris speed
    time = d / (a + b)                     # collision time
    paris = time * f                       # paris flight distant
    print(f"#{tc} {paris}")