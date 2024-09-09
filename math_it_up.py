def is_even(number):
    """
    Determine if a number is even.
    """
    return number % 2 == 0

def is_odd(number):
    """
    Determine if a number is odd.
    """
    return number % 2 != 0

def mean(numbers):
    """
    Calculate the mean of a list of numbers.
    """
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Calculate the median of a list of numbers.
    """
    numbers.sort()
    if len(numbers) % 2 == 0:
        return mean([numbers[len(numbers) // 2], numbers[len(numbers) // 2 - 1]])
    else:
        return numbers[len(numbers) // 2]

def mode(numbers):
    """
    Calculate the mode of a list of numbers.
    """
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    max_count = max(counts.values())
    return [number for number, count in counts.items() if count == max_count]