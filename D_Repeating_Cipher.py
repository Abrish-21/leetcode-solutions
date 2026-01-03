def decipher():
    l = int(input())
    word = str(input())
    i = 0
    cipher_word = ""
    count = 0
    while  i < l:
        cipher_word += word[i]
        i += count + 1
        count += 1
    return cipher_word
print(decipher())

