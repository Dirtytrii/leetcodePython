class Kmp:
    dp = []
    pat = ''

    def __init__(self, pat):
        self.pat = pat
        M = len(pat)
        self.dp = [[0] * 256] * M

        self.dp[0][ord(self.pat[0])] = 1
        X = 0

        for j in range(1, M):
            for c in range(256):
                if ord(self.pat[j]) == c:
                    self.dp[j][c] = j + 1
                else:
                    self.dp[j][c] = self.dp[X][c]
            X = self.dp[X][ord(self.pat[j])]

    def search(self, txt):
        M, N = len(self.pat), len(txt)
        j = 0

        for i in range(N):
            j = self.dp[j][ord(txt[i])]
            if j == M:
                return i - M + 1

        return -1


out_txt = input()
out_pat = input()

kmp = Kmp(out_pat)

print(kmp.search(out_txt))
