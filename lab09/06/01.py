def gen(x) :
    yield x
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        yield x
s = int(input())
print(*gen(s))