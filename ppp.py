class Person:
	gender = input("your gender:")
	name = input("your name:")
	height = int(input("your height:"))
	weight = int(input("your weight:"))


	def eat(self, food):
		self.weight += food
		return self.weight


	def run(self, hours):
		self.weight -= hours * 1


	def change_name(self, name):
		self.name = name


Peter = Person()
mary = Person()

d = Peter.weight
a = Peter.eat(1)
b = mary.weight + 1
n = mary.eat(10)

print(d)
print(a)
print(b)
print(n)