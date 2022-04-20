def palindrome(s, l, r, cnt):
    while l < r:
        if s[l] == s[r]:
            pass
        else:
            if cnt == 0:
                a = palindrome(s, l, r-1, 1)
                b = palindrome(s, l+1, r, 1)
                if a == 0 or b == 0:
                    return 1
                else:
                    return 2
            else:
                return 2
        l += 1
        r -= 1
    return 0

t = int(input())
for _ in range(t):
    s = input()
    result = palindrome(s, 0, len(s)-1, 0)
    print(result)
