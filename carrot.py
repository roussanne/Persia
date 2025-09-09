t = int(input().strip())

for tc in range(1, 1 + t):

    n = int(input().strip())
    arr = list(map(int, input().split()))

    max_cnt = 1   # 최소 길이
    cnt = 1       # 연속 증가 길이

    for i in range(1, n):

        if arr[i] > arr[i-1]:   # 증가하는 경우
            cnt += 1

            if cnt > max_cnt:   # 최대값 갱신
                max_cnt = cnt

        else:                   # 증가가 끊기면  reset
            cnt = 1

    print(f"#{tc} {max_cnt}")



t = int(input())

for tc in range(1, 1+t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    maxi = 1
    
    for i in range(n-1):
        
        if arr[i] < arr[i+1]:
            cnt += 1
            
            if maxi < cnt:
                maxi = cnt
        
        else:
            cnt = 1
    
    
    print(f"#{tc} {maxi}")

# n-1로 받아야 초과 안됨 maxi 1로 해서 i, i+1 비교하면 다음값이 연속인지 확인가능
# 연속 끊겨서 else 되면 1로 초기화



"""
9367

영준이는 당근 크기 선별기를 이용해 수확한 순서대로 당근의 크기를 기록하였다.
이 당근 선별기에는 특별한 기능이 있는데 연속으로 당근의 크기가 커진 경우 그 개수를 알려준다.
당근의 크기가 수확한 순서로 주어질 때, 선별기가 알려준 연속으로 커지는 당근의 갯수는 최대 얼마인지 확인하기 위한 프로그램을 만드시오.
연속으로 커지지않는 경우 구간의 최소 길이는 1이다.
N개의 당근을 수확하며, 당근의 크기 C는 1부터 10까지의 정수로 정해진다.
5<=N<=1000, 1<=C<=10



입력
첫 줄에 테스트케이스의 개수 T, 다음 줄 부터 테스트케이스별로 첫 줄에 당근 개수 N, 다음 줄 당근의 크기 C를 의미하는 N개의 정수가 주어진다.

4
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1
8
1 2 1 2 3 1 2 1



출력
#테스트케이스번호와 연속으로 커지는 당근 개수의 최대값을 출력한다.

#1 5
#2 3
#3 1
#4 3


"""