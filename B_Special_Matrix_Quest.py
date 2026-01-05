def specialElement():
    t= int(input())
    matrix = []
    for _ in range(t):
        row = list(map(int, input().split()))
        matrix.append(row)
        n = len(matrix[0])
    valid_element = 0
    for i in range(n):
        for j in range(n):
            if i ==j or (i + j == n-1) or (i == int((n-1) / 2)) or (j == int((n-1) / 2)):
                valid_element += matrix[i][j]
    return valid_element
print(specialElement())