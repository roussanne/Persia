t = int(input())

for i in range(1, t + 1):
    asdf = list(map(int, input().split()))
    v = 0
    for j in range(10):
        v += asdf.pop()
    avg = v / 10
    print(f"#{i} {round(avg)}")
