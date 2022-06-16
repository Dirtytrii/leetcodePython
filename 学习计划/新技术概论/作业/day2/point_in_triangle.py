from math import ceil


# 通过三个点求面积
def areaOfTri(x1, y1, x2, y2, x3, y3):
    return round(0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)), 4)


def isInTri(triangle, x, y):
    # 表示三角形的三个点
    x1, y1 = triangle[0][0], triangle[0][1]
    x2, y2 = triangle[1][0], triangle[1][1]
    x3, y3 = triangle[2][0], triangle[2][1]

    # 点x,y和1，2
    s_a = areaOfTri(x, y, x1, y1, x2, y2)
    # 点x,y和2，3
    s_b = areaOfTri(x, y, x2, y2, x3, y3)
    # 点x,y和1，3
    s_c = areaOfTri(x, y, x1, y1, x3, y3)
    # 三角形面积
    s = areaOfTri(x1, y1, x2, y2, x3, y3)

    return s == round(s_a + s_b + s_c, 4)


if __name__ == '__main__':
    triangle = [[1.5, 1.5], [1.5, 6.8], [6.8, 1.5]]
    count = 0
    # 找到最左端的X,向下取整
    left_point = int(min((triangle[0])[0], (triangle[1])[0], (triangle[2])[0]))
    # 找到最右端的X，向上取整
    right_point = ceil(max((triangle[0])[0], (triangle[1])[0], (triangle[2])[0]))
    # 找到最上端的Y，向上取整
    up_point = ceil(max((triangle[0])[1], (triangle[1])[1], (triangle[2])[1]))
    # 找到最下端的Y，向下取整
    down_point = int(min((triangle[0])[1], (triangle[1])[1], (triangle[2])[1]))

    # 将xY值限制在这个矩形范围,步长为1
    for x in range(left_point, right_point + 1, 1):
        for y in range(down_point, up_point + 1, 1):
            if isInTri(triangle, x, y):
                count += 1
    print(count)
