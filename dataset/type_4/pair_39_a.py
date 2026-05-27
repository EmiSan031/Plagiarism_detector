def running_sum(numbers):
    result = []
    total = 0
    for number in numbers:
        total += number
        result.append(total)
    return result

def running_max(numbers):
    result = []
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
        result.append(current_max)
    return result

def running_product(numbers):
    result = []
    product = 1
    for number in numbers:
        product *= number
        result.append(product)
    return result

def differences(numbers):
    result = []
    for i in range(1, len(numbers)):
        result.append(numbers[i] - numbers[i - 1])
    return result

data = [3, 1, 4, 1, 5, 9, 2, 6]
print(running_sum(data))
print(running_max(data))
print(running_product([1, 2, 3, 4, 5]))
print(differences(data))
