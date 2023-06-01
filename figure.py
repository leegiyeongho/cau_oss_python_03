"""
line 클래스를 통해 선의 길이를 설정/참조한다
area_square, area_circle, area_regular_triangle, area_rectangle, area_ellipse, area_right_triangle 함수를 통해
정사각형, 원, 정삼각형, 직사각형, 타원, 직각 삼각형의 넓이를 구할 수 있다.

"""
import math

class line:
    """
    figure_main 에서 width, height를 정의하기 위해 사용되는 객체
    """
    def __init__(self, value1=0, value2=0):
        """클래스의 생성자로서 저장하고 있는 __width, __height에 값을 대입할 수 있다
        Arg:
            value1(기본값=0): width에 대입할 값, value2(기본값=0): height에 대입할 값
        Returns:
            아무 값도 리턴하지 않음 (혹은 공란으로 비워둠)
        Examples:
            >>> width = line(10,9) # width 객체에 line 클래스를 지정하고, __width에 10, __height에 9를 대입함
        """
        self.__width = value1
        self.__height = value2

    def set_length(self, value1, value2):
        """저장하고 있는 __width에 value1, __height에 value2를 대입한다.
        Args:
            value1: __width 대입할 값, value2: __height 대입할 값
        Returns:
            아무 값도 리턴하지 않음 (혹은 공란으로 비워둠)
        Examples:
            >>> myline.set_width(10,9) # myline의 __width 필드에 10, __height 필드에 9를 대입한다.
        """
        self.__width = value1
        self.__height= value2
    
    def get_length(self):
        """저장하고 있는 __width, __height를 반환한다.
        Args:
            아무 값도 필요하지 않음 (혹은 공란으로 비워둠)
        Returns:
            __width, __height
        Examples:
            >>> myline.get_length() # myline의 __width, __height 필드의 값을 반환한다.
        """
        return self.__width, self.__height
    
def area_square(width):
    """width를 한변으로 하는 정사각형의 넓이를 반환한다.
    Args:
        width: 정사각형 한변의 길이
    Returns:
        area: width를 한변으로 하는 정사각형의 넓이
    Examples:
        >>> area_square(10) # 한변의 길이가 10인 정사각형의 넓이를 반환한다.
    """
    area = width * width
    return area

def area_circle(width):   
    """width를 반지름으로 하는 원의 넓이를 반환한다.
    Args:
        width: 반지름
    Returns:
        area: width를 반지름으로 하는 원의 넓이
    Examples:
        >>> area_circle(10) # 반지름 10인 원의 넓이를 반환한다.
    """
    area = width * width * math.pi
    return area

def area_regular_triangle(width):
    """width를 한변으로 하는 정삼각형의 넓이를 반환한다.
    Args:
        width: 정삼각형 한변의 길이
    Returns:
        area: width를 한변으로 하는 정삼각형의 넓이
    Examples:
        >>> area_regular_triangle(10) # 한변의 길이가 10인 정삼각형의 넓이를 반환한다.
    """
    area = math.sqrt(3) /4 * width * width
    return area

def area_rectangle(width,height):
    """widgth와 height를 두 변으로 하는 직사각형의 넓이를 반환한다.
    Args:
        width: 직사각형 가로 길이
        height: 직사각형 세로 길이
    Returns:
        area: width와 height를 두 변으로 하는 직사각형의 넓이
    Examples:
        >>> area_rectangle(10,9) # 가로 길이가 10, 세로 길이가 9인 직사각형의 넓이를 반환한다.
    """
    area = width * height
    return area

def area_ellipse(width,height):   
    """width와 height를 가로, 세로 반지름으로 하는 타원의 넓이를 반환한다.
    Args:
        width: 가로 반지름, height: 세로 반지름
    Returns:
        area: widgth와 height를 가로, 세로 반지름으로 하는 타원의 넓이
    Examples:
        >>> area_ellipse(10,9) # 가로 반지름 10, 세로 반지름이 9인 타원의 넓이를 반환한다.
    """
    area = width * height * math.pi
    return area

def area_right_triangle(width,height):
    """width를 밑변으로, height를 높이로 하는 삼각형의 넓이를 반환한다.
    Args:
        width: 삼각형 밒변의 길이, height: 삼각형의 높이
    Returns:
        area: width를 밑변으로, height를 높이로 하는 삼각형의 넓이
    Examples:
        >>> area_right_triangle(10,9) # 밑변의 길이가 10, 높이가 9인 삼각형의 넓이를 반환한다.
    """
    area = width * height / 2
    return area


