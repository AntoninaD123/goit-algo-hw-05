import timeit

# -------------------------------
# Load texts (article 1 and article 2)
# -------------------------------
with open("article_1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("article_2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()


# -------------------------------
# Knuth-Morris-Pratt (KMP) algorithm
# -------------------------------
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j  # found
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1  # not found


# -------------------------------
# Rabin-Karp algorithm
# -------------------------------
def rabin_karp_search(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    hpattern = 0
    htext = 0
    h = 1

    for i in range(m-1):
        h = (h * base) % mod

    for i in range(m):
        hpattern = (base * hpattern + ord(pattern[i])) % mod
        htext = (base * htext + ord(text[i])) % mod

    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            htext = (base * (htext - ord(text[i]) * h) + ord(text[i+m])) % mod
            if htext < 0:
                htext += mod
    return -1


# -------------------------------
# Boyer-Moore algorithm
# -------------------------------
def boyer_moore_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0

    # Build bad character table
    bad_char = [-1] * 256
    for i in range(m):
        bad_char[ord(pattern[i])] = i

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return -1


# -------------------------------
# Substring selection
# -------------------------------
# For text1
pattern1_exist = "algorithms"         # existing substring
pattern1_fake = "qwerty123"           # fake substring

# For text2
pattern2_exist = "unrolled list"      # existing substring
pattern2_fake = "abcdefxyz"           # fake substring


# -------------------------------
# Time measurement function
# -------------------------------
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1)


# -------------------------------
# Run and compare
# -------------------------------
algorithms = {
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp_search,
    "Boyer-Moore": boyer_moore_search
}

texts = [
    ("Article 1", text1, pattern1_exist, pattern1_fake),
    ("Article 2", text2, pattern2_exist, pattern2_fake)
]

for text_name, text, pat_exist, pat_fake in texts:
    print(f"\n--- {text_name} ---")
    for name, func in algorithms.items():
        time_exist = measure_time(func, text, pat_exist)
        time_fake = measure_time(func, text, pat_fake)
        print(f"{name} (existing): {time_exist:.6f}s, (fake): {time_fake:.6f}s")
