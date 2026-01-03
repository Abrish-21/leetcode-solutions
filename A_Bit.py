def bit():
    t = int(input())
    count_no = 0
    for _ in range(t):
        statement = str(input())
        if statement == "X++" or statement == "++X":
            count_no += 1
        else:
            count_no -= 1
    return count_no
    
print(bit())