from ph_units import converter

x = converter.convert(594.445, "kBtu/ft2", "kWH/ft2")
y = converter.convert(594.445, "kBtu/ft2", "kWh/m2")
z = converter.convert(594.445, "kBtu/ft2", "Wh/ft2")
print(x)
print(y)
print(z)
