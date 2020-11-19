'''
�������� ����� Circle, �������������� ����. � ����� ������ ������ ����:

����������� ����������� ������ ������ Point, ����� ������ �����, � �����, ������ �����;
�������� center � radius, ������������ ����� � ������ ����� ��������������;
����� square, ������� ���������� ������� �����.
����� Point �� ������ ������������ � ����� ���� ��� ���������� (�.�. ��� �� ����� ��� ������).

circ = Circle(Point(0, 3), 4)
circ.radius == 4
circ.center.x == 0

Circle(Point(0, 0), 0).square() == 0
'''

class Circle:
    
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
    def square(self):
        return 3.14 * self.radius**2