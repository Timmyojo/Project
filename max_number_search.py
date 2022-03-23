def max_number(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

num = max_number([4, 90])
print(num)

