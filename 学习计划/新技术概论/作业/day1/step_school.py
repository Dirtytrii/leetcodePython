def count_of_step():
    x = 7

    while not (x % 2 == 1 and x % 3 == 2 and x % 5 == 4 and x % 6 == 5):
        x += 7
    return x


if __name__ == '__main__':
    print(count_of_step())
