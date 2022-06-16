n, m = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input()))

r, c = map(int, input().split())
shocket = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    shocket[i] = list(map(int, input()))

findAns = False


def isNotIligal(i, j):
    if i + r > n or j + c > m:
        return False

    temp = j

    # 开始遍历
    for row in range(r):
        for col in range(c):
            if board[i][j] != shocket[row][col]:
                return False
            j += 1
        i += 1
        # 重置列坐标
        j = temp

    return True



for i in range(n):
    for j in range(m):
        if isNotIligal(i, j):
            print(i, end=' ')
            print(j)
            findAns = True
            break
    if findAns:
        break

if not findAns:
    print('No')
