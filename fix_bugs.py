def multi(l_st):
    if len(l_st) > 0:
        a = 1
        for i in l_st:
            a = a * i
        return a
def add(l_st):
    if len(l_st) > 0:
        a = 0
        for i in l_st:
            a += i
        return a
def reverse(string):
    return string[::-1]