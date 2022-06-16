for i in range(3000, 4000):
    temp = i

    if temp % 5 == 1:
        temp -= 1
        temp -= temp / 5
        if temp % 5 == 2:
            temp -= 2
            temp -= temp / 5
            if temp % 5 == 3:
                temp -= 3
                temp -= temp / 5
                if temp % 5 == 4:
                    temp -= 4
                    temp -= temp / 5
                    if temp % 5 == 0:
                        print(i)
                        break
