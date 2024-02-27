n = int(input())


def rhombus_printer_upper(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '* ' * (i + 1))


def rhombus_printer_bottom(size):
    for i in range(size):
        print(' ' * (i + 1) + '* ' * (size - i - 1))


rhombus_printer_upper(n)
rhombus_printer_bottom(n)
