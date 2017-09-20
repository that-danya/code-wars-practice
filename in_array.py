def in_array(array1, array2):
    r = set()
    for a in array1:
        for b in array2:
            if a in b:
                r.add(a)
                break
    return sorted(r)
