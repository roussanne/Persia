t = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, t + 1):  # 케이스 반복
    k, n, m = map(int, input().split())         # k: 최대 이동거리, n: 종점, m: 충전소 수
    chargers = list(map(int, input().split()))  # 충전소 위치 리스트(정렬 여부 상관 없음)
    
    x = 0      # 현재 위치 (출발점 0)
    cnt = 0    # 충전 횟수 누적
    
    if n <= k:            # 한 번에 도착 가능한 경우 충전 불필요
        cnt = 0
        continue          # 결과 출력으로 바로 이동
    
    else:
        while x + k < n:               # 현재위치가 +k가 종점에 갈때 까지 반복   
            farthest = -1              # 후보가 없음을 나타낼 초기값
            
            for c in chargers:         # 모든 charger 리스트값 확인함
                if x < c <= x + k:     # 현재 위치보다 크고 k 이내에 있고
                    if c > farthest:   # 현재 최댓값보다 크면
                        farthest = c   # 갱신 farthest는 1번에 갈 수 있는 가장 먼 정류장
            
            
            if farthest != -1: #  farthest 값 갱신했으면 
                x = farthest   # 현재위치 = 찾아낸 가장 먼 충전소
                cnt += 1       # 충전 횟수 증가
            
            else:              # -1 = 충전소 못찾았음
                cnt = 0
                break      # while 문 탈출하고 결과 출력 cnt 변화 없으므로 0
    
    
    print(f"#{tc} {cnt}")  # 결과 출력


# 한번에 도착지점 가면 else 넘기고 프린트
# 아니면 k만큼 이동해서 도착 할떄 까지
# 정류소 리스트에서 현재위치에서 +k 안에 있는 충전소 뽑아서 가장 큰 값 찾기
# 정류소 찾으면 farthest는 한번에 갈 수 있는 가장 먼 충전소 됨 count ++ 충전홧수 증가
# else 중간에 막혔다는 뜻 카운트 초기화 하고  while 탈출해서 0출력











"""
4831

A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.



[예시]



다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.




[입력]


첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )


3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17



[출력]


#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.


#1 3
#2 0
#3 4


"""


t = int(input())

for tc in range(1, 1 + t):
    k, n, m = map(int,input().split())
    charge = list(map(int,input().split()))

    x = 0
    cnt = 0

    if k >= n:
        cnt = 0

    else:
        while x + k < n:
            maxi = -1

            for i in charge:
                if x < i <= x + k:
                    if maxi < i:
                        maxi = i
            
            if maxi != -1:
                x = maxi
                cnt += 1

            else:
                cnt = 0
                break

    print(f"#{tc} {cnt}")  # 결과 출력
