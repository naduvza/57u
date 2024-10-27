def reverse_generator():
    for i in range(10, 0, -1):
        yield i

for num in reverse_generator():
    print(num)
