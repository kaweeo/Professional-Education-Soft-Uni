def rectangle(length, width) -> str:
    if not (isinstance(length, int) and isinstance(width, int)):
        return "Enter valid values!"
    length, width = int(length), int(width)
    area = length * width
    perimeter = 2 * length + 2 * width
    return f'Rectangle area: {area}\nRectangle perimeter: {perimeter}'


print(rectangle(2, 10))