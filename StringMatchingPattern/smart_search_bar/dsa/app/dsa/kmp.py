def pfun(pattern: str):
    n = len(pattern)
    prefix_lst = [0]*(n)
    k = 0
    for q in range(1, n):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix_lst[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        prefix_lst[q] = k
    return prefix_lst

def kmp(text: str, pattern: str) -> tuple[list[int], int]:
    """Implementation of string matching pattern.
    
    Knuth Morris Pratt
    """

    n = len(text)
    m = len(pattern)

    prefix_lst = pfun(pattern)
    q = 0
    matches: list[int] = []
    comparisons = 0

    for i in range(n):
        comparisons += 1
        while q > 0 and pattern[q] != text[i]:
            q = prefix_lst[q -1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = prefix_lst[q - 1]
    return matches, comparisons
