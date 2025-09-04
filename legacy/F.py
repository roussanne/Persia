t = int(input())

for i in range(1, 1+t):
    n, k = map(int, input().split())
    score = []
    F = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    grade = n // 10                                      # n/10명 학생에게 동일평점

    for j in range(n):  
        mid, fin, asg = map(int, input().split())
        total = mid*0.35 + fin*0.45 + asg*0.20           # 총점계산
        score.append(total)                              # 총점 list에 저장
    req = score[k-1]                                     # k번째 학생 총점
    rerange = sorted(score, reverse=True)                # 점수별 높은순으로 정렬
    position = rerange.index(req)                        # k번째 학생 의 등수
    a = F[position // grade]                             # 등수구간별 평점 적용

    print(f"#{i} {a}")