t = int(input())

for i in range(1, 1+t):
    n, k = map(int, input().split())
    score = []
    F = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    grade = n // 10

    for j in range(n):
        mid, fin, asg = map(int, input().split())
        total = mid*0.35 + fin*0.45 + asg*0.20
        score.append(total)
    req = score[k-1]
    rerange = sorted(score, reverse=True)
    position = rerange.index(req)
    a = F[position // grade]

    print(f"#{i} {a}")