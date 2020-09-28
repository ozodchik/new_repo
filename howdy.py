class color():
	red = 0
	green = 0
	blue = 0


	def __init__(self, r, g, b):
		red = r
		green = g
		blue = b
	

	def tohex(self):
		return "#%02x%02x%02x" % (red, green, blue)

gray = color(80, 80, 80)

print(gray)