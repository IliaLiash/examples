from collections import namedtuple
from operator import attrgetter

def sort_by_ext(files):
    File = namedtuple('File', ['name', 'extens'])
    for i in range(len(files)):
        files[i] = File(files[i][:files[i].rfind('.')], files[i][files[i].rfind('.'):])
    files.sort(key=attrgetter('extens', 'name'))
    res = []
    k = 0
    for i in range(len(files)):
        if len(files[i].name) != 0:
            res.append(files[i].name + files[i].extens)
        else:
            res.insert(k, files[i].name + files[i].extens)
            k += 1
    return res
    
if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    assert sort_by_ext(["1.cad","2.bat","1.aa","1.bat"]) == ["1.aa","1.bat","2.bat","1.cad"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
