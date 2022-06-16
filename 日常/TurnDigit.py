year = 2019
ans = ''

while year != 0:
    temp = year % 26
    ans += str(temp) + ' '
    year = year // 26

print(ans)
