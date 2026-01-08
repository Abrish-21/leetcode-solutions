r,c = map(int, input().split())

directions = [(1,0), (0,1), (-1, 0), (0, -1), (1,-1), (-1, 1), (-1, -1), (1,1)]
digits = ['1','2','3','4','5','6','7','8']

matrix = []
for _ in range(r):
    row =  str(input())
    matrix.append([x for x in row])


def inbound(row, col):
    if  0 <= row < r and 0 <= col < c:
        return True
    else:
        return False

valid = True 

for i in range(r):
    for j in range(c):

        # case 1 for the cell to be "." 
        if matrix[i][j] == ".":
            for row,col in directions:
                new_row = row + i 
                new_col = col + j
                
                if inbound(new_row, new_col):
                    if matrix[new_row][new_col] == "*" :
                        valid = False
        elif matrix[i][j] in digits:
            bomb_count = 0
            for row, col in directions:
                new_row = i + row
                new_col = j + col
                if inbound(new_row, new_col) and matrix[new_row][new_col] == '*':
                    bomb_count += 1

            if bomb_count != int(matrix[i][j]) or bomb_count == 0 :
                valid = False
        else:
            continue 


if valid:
    print("YES")
else:
    print("NO")

                    

        


            
