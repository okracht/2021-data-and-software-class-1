
absolute_zero_c = -273.15

def fahr_to_celsius(temperature):
    return((temperature -32) * (5/9))

def celsius_to_kelvin(temperature):
    # Pre-conditions:
    assert(temperature >= absolute_zero_c)
    return(temperature+273.15)

def fahr_to_kelvin(temperature_fahr):
    temperature_c = fahr_to_celsius(temperature_fahr)
    temperature_k = celsius_to_kelvin(temperature_c)
    assert(temperature_k >= 0.0)
    return temperature_k


print("freezing point:", fahr_to_celsius(32))
print("boiling point:", fahr_to_celsius(212))
print("cold point:", fahr_to_kelvin(-212))

# Post-conditions:
assert (fahr_to_celsius(32) == 0.0)
assert (fahr_to_celsius(212) == 100.0)

assert (celsius_to_kelvin(0.0) == 273.15)
assert (celsius_to_kelvin(100.0) == 373.15)

assert (fahr_to_kelvin(32) == 273.15)

# Invariants:
assert (absolute_zero_c == -273.15)
fahr_to_kelvin(32)
assert (absolute_zero_c == -273.15)


def normalize_rectangle(rect):
    """Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.
    Input should be of the format (x0, y0, x1, y1).
    (x0, y0) and (x1, y1) define the lower left and upper right corners
    of the rectangle, respectively."""
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates'
    assert y0 < y1, 'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dy) / dx
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)


print (normalize_rectangle((0.0, 0.0, 5.0, 1.0)))


def get_total(values):
    assert len(values) > 0
    total = 0
    index = 0

    for element in values:
        assert int(element)
        assert total >= 0
        total = total + element
        index = index + 1

    assert total > 0
    return total

print (get_total((1,2,4,5,7,8,68,3,2,5)))

