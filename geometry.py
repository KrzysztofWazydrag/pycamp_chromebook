from math import pi

#pole koła
def circle_area(r: float) ->float:
    return pi * r ** 2

#obwód koła
def circle_circumference(r: float) -> float:
    return 2 * pi * r

#obwód trójkąta równobocznego
def triangle_equilateral_circumference(a: float) -> float:
    return 3 * a

#pole trójkąta równobocznego
def triangle_equilateral_area(a: float) -> float:
    return a ** 2 * sqrt(3) / 4

def middle_of_segment(x1:int, y1: int, x2: int, y2: int) -> float:
    return (x1 +x2) / 2 , (x1+y2) /2

def segment_length(x1, y1: int, x2: int, y2:int) -> float:
    return(sqrt((x1 -x2) ** 2 + (y1 - y2) ** 2)
