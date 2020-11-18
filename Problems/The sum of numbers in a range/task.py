def range_sum(numbers, start, end):
    sum1 = 0
    for num in numbers:
        if start <= num <= end:
            sum1 += num
    return sum1


input_numbers = [int(x) for x in input().split()]
a, b = input().split()
print(range_sum(input_numbers, int(a), int(b)))
