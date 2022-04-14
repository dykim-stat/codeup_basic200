M = [[0 for j in range(10)] for i in range(10)]
for i in range(len(M)):
    value = list(map(int, input().split(' ')))
    M[i] = value

xi, yi = 1, 1
M[xi][yi] = 9

while True:
    if M[xi][yi+1] != 1:
        if M[xi][yi+1]==2:
            M[xi][yi+1] = 9
            break
        M[xi][yi+1] = 9
        xi, yi = xi, yi+1

    elif M[xi+1][yi] != 1:
        if M[xi+1][yi]==2:
            M[xi+1][yi] = 9
            break
        M[xi+1][yi] = 9
        xi, yi = xi+1, yi

    else:
        break

for i in range(10):
    for j in range(10):
        print(M[i][j], end=' ')
    print()