def squares_generator():
    for i in range(1, 6):
        yield i, i ** 2

for num, square in squares_generator():
    print(num, square)
