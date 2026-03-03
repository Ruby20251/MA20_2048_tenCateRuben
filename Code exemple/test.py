# for row in range(4):
#     for col in range(4):
#         print("0", end=" ")
#     print()

# Grille de jeu (tableau 2D)

# for row in range(4):
#     for col in range(4):
#         print(game[row][col], end=" ")
#     print()

def pack4(a, b, c, d):
    if a == 0:
        a, b, c, d = b, c, d, 0

    elif b == 0:
        b, c, d = c, d, 0
    
    elif c == 0:
        c, d = d, 0
    
    elif a == b:
        a, b, c, d = 2*a, c, d, 0

    elif b == c:
        b, c, d = 2*b, d, 0
    
    elif c == d:
        c, d = 2*c, 0
        
    return a, b, c, d


print(pack4(0, 2, 4, 4))
print (pack4(2, 4, 4, 0))
print (pack4(2, 2, 2, 2))


