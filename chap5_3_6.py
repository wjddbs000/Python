def test():
    print("A지점")
    yield 1
    print("B지점")
    yield 2
    print("C지점")

output = test()

print("D지점")
a= next(output)
print(a)

print("E지점")
b =next(output)
print(b)