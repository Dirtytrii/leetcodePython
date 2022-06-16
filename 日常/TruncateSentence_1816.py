def truncateSentence(self, s: str, k: int) -> str:
    bef_res = s.split()
    res = ''

    for i in range(0, k):
        if i == k - 1:
            res += bef_res[i]
        else:
            res += bef_res[i] + ' '
    return res
