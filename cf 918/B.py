n = int(input())
for i in range(n):
    rows = 3
    cols = 3
    mat = []
    for i in range(rows):
        row = input()
        mat.append(list(row))

    for i in range(3):
        for j in range(3):
            if mat[i][j]=='?':
                row = i
                break
    dummy = ['A','B','C']
    
    ans = set(dummy)-set(mat[row])
        
    print(*ans)

