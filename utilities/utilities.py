def find_between(first, last, s, include_begining=False, find_last_match=False):
    try:
        if first not in s:
            return None, 0

        if not include_begining:
            start = s.index(first) + len(first)
        else:
            start = s.index(first)

        if find_last_match:
            end = s.rindex(last, start)
        else:
            end = s.index(last, start)
        return s[start:end], s.index(s[start:end])
    except ValueError:
        return None, 0
