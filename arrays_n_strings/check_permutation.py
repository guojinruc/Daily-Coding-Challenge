# Two strings a and b, check if a is a permutation of b

from collections import defaultdict
from typing import Dict
from math import abs

def count_chars_counter(s: str) -> defaultdict:
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1
    return counter

def count_chars_dict(s: str) -> Dict:
    counter = dict()
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    return counter

def check_permutation(a: str, b: str) -> bool:
    counter_a = count_chars_counter(a)
    counter_b = count_chars_counter(b)
    n_distinct_c = len(counter_a) == len(counter_b)
    n_per_c = list(
        map(
            lambda c: abs(counter_a.get(c,0) - counter_b.get(c,0)),
            counter_a.keys()))
    all_a_in_b = sum(n_per_c) == 0
    return n_dinstinct_c and all_a_in_b