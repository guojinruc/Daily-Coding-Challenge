def urlify_extra_space(s: str, n: int) -> str:
    """
    Replaces all apces with '%20'
    
    Args:
        s: Input string that contains spaces.
        n: True length of the string.
    """
    s = s[:n]
    n_spaces = sum([1 for c in s if c == ' '])
    
    if n_spaces == 0:
        return s

    replace = '%20'
    n_chars = n - n_spaces
    len_url = n_chars + 3*n_spaces
    url = [''] * len_url
    space_counter = 0

    for i, c in enumerate(s):
        pos = i + space_counter*2
        if c == ' ':
            url[pos: pos+len(replace)] = replace
            space_counter += 1
        else:
            url[pos] = c
    return ''.join(url)


def urlify(s:str, n: int) -> str:
    """Replace all spaces with '%20' in place"""
    n_spaces = sum([1 for c in s[:n] if c == ' '])

    if n_spaces == 0:
        return s
    
    replace = '%20'
    url = list(s[:n]) + ['']*n_spaces*2
    len_url = len(url)
    space_counter = 0
    for i, c in enumerate(url[:n][::-1]):
        pos = len_url - i - 2*space_counter
        if c == ' ':
            url[pos-len(replace) : pos] = replace
            space_counter += 1
        else:
            url[pos-1] = c
    return ''.join(url)


if __name__ == '__main__':
    urlify('  abc', 5)

def test_no_space():
    assert urlify('abc', 3) == 'abc'

def test_space_at_start():
    assert urlify('  abc', 5) == r'%20%20abc'

def test_space_at_end():
    assert urlify('Mr John Smith   ', 13) == 'Mr%20John%20Smith'