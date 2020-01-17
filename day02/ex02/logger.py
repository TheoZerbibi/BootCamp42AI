import time, os
from random import randint

def log(func):
	def msg(*args):
		start = time.time()
		original_result = func(*args)
		end = time.time()
		diff = end - start
		res = f"{diff:.03f} s" if diff > 0.01 else f"{(diff  * 1000):.03f} ms]"
		with open("machine.log", "a") as log_file:
			log_file.write(f"({os.getlogin()}) Running: {func.__name__}     [exec-time = {res}]\n")
		return original_result
	return msg


class CoffeeMachine:
	water_level = 100
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")


if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)
