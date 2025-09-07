letter = (input().strip())
k = int(input())
shift = k % 26
char = (ord(letter) - ord('a') + shift) % 26
print (chr(char + 97))