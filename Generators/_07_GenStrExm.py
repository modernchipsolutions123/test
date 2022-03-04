def multiple_yield():
    str1 = "Sai"
    yield str1

    str2 = "Kumar"
    yield str2

    str3 = "Shiva"
    yield str3

    str4 = "S.K.S"
    yield str4

obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

