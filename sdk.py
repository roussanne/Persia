t = int(input())

for tc in range(1, t+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    
    result = 1
    
    for r in range(9):
        if len(set(board[r])) != 9:
        
            result = 0
            break


    if result:
        
        for c in range(9):
            col = [board[r][c] for r in range(9)]
            
            if len(set(col)) != 9:
                result = 0
                break


    if result:
        for sr in range(0, 9, 3):
            for sc in range(0, 9, 3):
                
                box = []
                for r in range(3):
                    for c in range(3):
                        box.append(board[sr+r][sc+c])
                
                if len(set(box)) != 9:
                    result = 0
                    break
    
    
    print(f"#{tc} {result}")












# t = int(input())

# for tc in range(1, 1+t):
#     arrr = []
#     for i in range(9):
#         arr= list(map(int, input().split()))
#         arrr.append(arr)
    
    
    
#     # for j in range(9):
#     #     chk = 0
#     #     for k in range(9):
#     #         chk += arrr[j][k]
    
#     # if chk != 45:
#     #     break
    
#     # for q in range(9):
#     #     c = 0
#     #     c += arrr[q][0]
#     # if c != 45:
#     #     break
    
#     for w in range(0, 9, 3):
#         for e in range(3):
#             arrr[w][w+e]
    
#         # row(9) col(9) row(3)col(3)