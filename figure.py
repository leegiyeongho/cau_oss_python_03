"""
line 클래스를 통해 선의 길이를 설정/참조한다
area_square, area_circle, area_regular_triangle 함수를 통해 정사각형과 원과 정삼각형의 넓이를 구할 수 있다.
"""
import math

class line:
    """
    figure_main 에서 length를 정의하기 위해 사용되는 객체
    """
    __length = 0
    """
    일반적으로는 접근 불가능한 변수 __length 설정
    """
    def __init__(self, value):
        """클래스의 생성자로서 저장하고 있는 __length에 값을 대입할 수 있다
        Arg:
            value: 대입할 값
        Returns:
            아무 값도 리턴하지 않음 (혹은 공란으로 비워둠)
        Examples:
            >>> length = line(10) # length 객체에 line 클래스를 지정하고, __length에 10을 대입함
        """
        self.__length = value

    def set_length(self, value):
        """저장하고 있는 __length에 value를 대입한다.
        Args:
            value: 대입할 값
        Returns:
            아무 값도 리턴하지 않음 (혹은 공란으로 비워둠)
        Examples:
            >>> myline.set_length(10) # myline의 __length 필드에 10을 대입한다.
        """
        self.__length = value
    
    def get_length(self):
        """저장하고 있는 __length를 반환한다.
        Args:
            아무 값도 필요하지 않음 (혹은 공란으로 비워둠)
        Returns:
            __length
        Examples:
            >>> myline.get_length() # myline의 __length 필드의 값을 반환한다.
        """
        return self.__length
    
def area_square(length):
    """length를 한변으로 하는 정사각형의 넓이를 반환한다.
    Args:
        length: 정사각형 한변의 길이
    Returns:
        area: length를 한변으로 하는 정사각형의 넓이
    Examples:
        >>> area_square(10) # 한변의 길이가 10인 정사각형의 넓이를 반환한다.
    """
    area = length * length
    return area

def area_circle(length):   
    """length를 반지름으로 하는 원의 넓이를 반환한다.
    Args:
        length: 반지름
    Returns:
        area: length를 반지름으로 하는 원의 넓이
    Examples:
        >>> area_circle(10) # 반지름 10인 원의 넓이를 반환한다.
    """
    area = length * length * math.pi
    return area

def area_regular_triangle(length):
    """length를 한변으로 하는 정삼각형의 넓이를 반환한다.
    Args:
        length: 정삼각형 한변의 길이
    Returns:
        area: length를 한변으로 하는 정삼각형의 넓이
    Examples:
        >>> area_regular_triangle(10) # 한변의 길이가 10인 정삼각형의 넓이를 반환한다.
    """
    area = math.sqrt(3) /4 * length * length
    return area