rooms = [
    {"name": "�����", "length": 6, "width": 4},
    {"name": "������� 1", "length": 5.5, "width": 4.5},
    {"name": "������� 2", "length": 5, "width": 4},
    {"name": "������� 3", "length": 7, "width": 6.3},
]

def square(d):
    d['square'] = d['length'] * d['width']
    return d

rooms = map(square, rooms)