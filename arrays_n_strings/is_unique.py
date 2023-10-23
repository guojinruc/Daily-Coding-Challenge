from collections import defaultdict

def is_unique_counter(s: str) -> bool:
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1
    for n in counter.values():
        if n > 1:
            return False
    return True

def is_unique_sort(s: str) -> bool:
    s = sorted(s)
    for i in range(len(s) -1):
        if s[i] == s[i+1]
            return False
    return True
