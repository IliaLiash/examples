def frequency_sorting(numbers):
    
    numbers = sorted(numbers)
    return sorted(numbers, key=numbers.count,reverse=True)