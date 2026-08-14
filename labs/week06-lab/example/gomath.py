def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

#หาพื่นที่สามเหลี่ยม
def triaingle(base, height) :
    """Calculates and displays triaingle area"""
    area = 0.5 * base * height
    print(f"Rectangle with hight {hight} and base {base}")
    print(f"Area = 0.5 *{hight} × {base} = {area}")
    print()

#หาพื้นที่วงกลม
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()