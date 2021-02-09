def swap_nodes(a):
    res = []
    k = 1
    for i in range(len(a)):
        try:
            if i % 2 == 0:
                res.append(a[k])
                k += 2
            else:
                res.append(a[i-1])
        except:
            res.append(a[-1])    
    
    return res


if __name__ == '__main__':
    print("Example:")
    print(list(swap_nodes([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(swap_nodes([1, 2, 3, 4])) == [2, 1, 4, 3]
    assert list(swap_nodes([5, 5, 5, 5])) == [5, 5, 5, 5]
    assert list(swap_nodes([1, 2, 3])) == [2, 1, 3]
    assert list(swap_nodes([3])) == [3]
    assert list(swap_nodes(["hello", "world"])) == ["world", "hello"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
