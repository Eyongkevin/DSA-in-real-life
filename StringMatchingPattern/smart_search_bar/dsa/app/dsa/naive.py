def naive(text: str, pattern: str) -> tuple[list[int], int]:
    """Implementation of search matching patter
    
    Naive
    """

    text_len = len(text) # n
    pattern_len = len(pattern) # m
    i = 0
    matches = []
    comparisons = 0

    while i < (text_len - pattern_len + 1): #alignment
        j = 0
        count = 0
        while j < pattern_len:
            comparisons += 1
            if text[i + j] == pattern[j]:
                count += 1
            j += 1
        if count == pattern_len:
            matches.append(i)
        i += 1
    return matches, comparisons