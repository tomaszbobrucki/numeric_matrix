def average_mark(*grades):
    total, num = 0, 0
    for i in grades:
        total += i
        num += 1
    return round(total / num, 1)


# print(average_mark(3, 4, 5, 3))
