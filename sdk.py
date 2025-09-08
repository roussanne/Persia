t = int(input())

for tc in range(1, 1+t):
    arrr = []
    for i in range(9):
        arr= list(map(int, input().split()))
        arrr.append(arr)
    
    
    
    # for j in range(9):
    #     chk = 0
    #     for k in range(9):
    #         chk += arrr[j][k]
    
    # if chk != 45:
    #     break
    
    # for q in range(9):
    #     c = 0
    #     c += arrr[q][0]
    # if c != 45:
    #     break
    
    for w in range(0, 9, 3):
        for e in range(3):
            arrr[w][w+e]
    
        # row(9) col(9) row(3)col(3)