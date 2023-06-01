# %%

"""
area_rectangle, area_right_triangle, area_ellipse 함수들에서
예외 발생 시 0이하의 값은 입력할 수 없습니다를 출력하도록 변경!
"""

import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    if width <= 0 or height <=0:
        raise ValueError
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("please input positive number for width and height")

myline.set_length(20, 30)
width, height = myline.get_length()
try:
    if width <= 0 or height <=0:
        raise ValueError
    triangle = figure.area_right_triangle(width, height)
    print(triangle)
except ValueError:
    print("please input positive number for width and height")
myline.set_length(30, 40)
width, height = myline.get_length()
try:
    if width <= 0 or height <=0:
        raise ValueError
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("please input positive number for width and height")