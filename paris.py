# 6019. 기차 사이의 파리

t = int(input())

for tc in range(1, t + 1):
    d, a, b, f = map(int, input().split())
    time = d / (a + b)
    paris = time * f
    print(f"#{tc} {paris}")