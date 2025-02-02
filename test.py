def f():
    yield 1
    yield 2
    
result = f()
print(result[0])