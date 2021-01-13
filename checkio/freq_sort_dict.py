def frequency_sort(items):
    d = {}
    for element in items:
        d[element] = items.count(element)
    
    result = []
    cache = []
    values = sorted(d.values())[::-1]
    i = 0
    
    for j in range(len(items)):  
        while i != len(values):
            if items[j] in cache:
                j += 1
                break
            elif items.count(items[j]) == values[i]:
                cache.append(items[j])
                count = 0
                while count != values[i]:
                    result.append(items[j])
                    count += 1    
                i += 1
            j += 1
    return result

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]    
    assert list(frequency_sort([4,6,2,2,2,6,4,4,4])) == [4,4,4,4,2,2,2,6,6]