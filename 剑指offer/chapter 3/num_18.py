def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        if not s[left].lower() == s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    print(isPalindrome('am?anaplan..acanalPanam?a'))
