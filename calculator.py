name = input("Введите своё имя:")
print("Привет", name)
what = input("выберите одну из этих способов: (+,-,*,/,**,//):")
first_number = float(input("Введите первое число:"))
second_number = float(input("Введите второе число:"))
if what == "+":
	print("Ответ:", first_number+second_number)
elif what == "-":
	print("Ответ:", first_number-second_number)
elif what == "*":
	print("Ответ:", first_number*second_number)
elif what == "/":
	print("Ответ:", first_number/second_number)
elif what == "**":
	print("Ответ:", first_number**second_number)
elif what == "//":
	print("Ответ:", first_number//second_number)
else:
	print("Выбран неверный способ")