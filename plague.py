t = int(input())
t =1
c =0
for tc in range(1, 1+t):
    size = int(input())
    asdff=[]
    asdf=[]
    centre = size//2

    for i in range(size):
        asdf = list(map(int,input()))
        asdff.append(asdf)

    for j in range(centre//2):
        c = asdf[centre-j] + asdf[centre] + asdf[centre+j]
            
        print(asdff)
        print(c)


        print(asdff[centre-1])
        print(asdff[centre])
        print(asdff[centre+1])


    1 4 0 5 4
    4 4 2 5 0
    0 2 0 3 2
    5 1 2 0 4
    5 2 2 1 2