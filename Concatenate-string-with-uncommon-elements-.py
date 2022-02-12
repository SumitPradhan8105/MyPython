def uncommonStr(str1, str2):
    s1 = set(str1)
    s2 = set(str2)
    common = list(s1 & s2)
    result = [ch for ch in s1 if ch not in common] + [ch for ch in s2 if ch not in common]
    return result
str1 = "abcdef"
str2 = "ghidefabc"
print(uncommonStr(str1, str2))
