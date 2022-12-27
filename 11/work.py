import copy

"""
items_default = [
	[79, 98],
	[54, 65, 75, 74],
	[79, 60, 97],
	[74],
]
"""
items_default = [
	[89, 84, 88, 78, 70],
	[76, 62, 61, 54, 69, 60, 85],
	[83, 89, 53],
	[95, 94, 85, 57],
	[82, 98],
	[69],
	[82, 70, 58, 87, 59, 99, 92, 65],
	[91, 53, 96, 98, 68, 82],
]


class Monkey:
	global inspects, items

	number       = 0
	operation_fn = lambda self,x:x
	divid_by     = 1
	to_true      = 0
	to_false     = 0

	def __init__(self, number, operation_fn, divid_by, to_true, to_false):
		self.number       = number
		self.operation_fn = operation_fn
		self.divid_by     = divid_by
		self.to_true      = to_true
		self.to_false     = to_false

	def inspect1(self) -> None:
		target = [item for item in items[self.number]]
		for i in target:
			inspects[self.number] += 1
			worried = self.operation_fn(i) // 3
			items[self.number].pop(0)

			if worried%self.divid_by == 0:
				items[self.to_true].append(worried)
			else:
				items[self.to_false].append(worried)

	def inspect2(self) -> None:
		target = [item for item in items[self.number]]
		for i in target:
			inspects[self.number] += 1
			worried = self.operation_fn(i)
			items[self.number].pop(0)

			if worried%self.divid_by == 0:
				items[self.to_true].append(worried)
			else:
				items[self.to_false].append(worried)


"""
monkeys = [
	Monkey(number=0, operation_fn=lambda x:x*19, divid_by=23, to_true=2, to_false=3),
	Monkey(number=1, operation_fn=lambda x:x+6 , divid_by=19, to_true=2, to_false=0),
	Monkey(number=2, operation_fn=lambda x:x*x , divid_by=13, to_true=1, to_false=3),
	Monkey(number=3, operation_fn=lambda x:x+3 , divid_by=17, to_true=0, to_false=1),
]
"""
monkeys = [
	Monkey(number=0, operation_fn=lambda x:x*5 , divid_by=7 , to_true=6, to_false=7),
	Monkey(number=1, operation_fn=lambda x:x+1 , divid_by=17, to_true=0, to_false=6),
	Monkey(number=2, operation_fn=lambda x:x+8 , divid_by=11, to_true=5, to_false=3),
	Monkey(number=3, operation_fn=lambda x:x+4 , divid_by=13, to_true=0, to_false=1),
	Monkey(number=4, operation_fn=lambda x:x+7 , divid_by=19, to_true=5, to_false=2),
	Monkey(number=5, operation_fn=lambda x:x+2 , divid_by=2 , to_true=1, to_false=3),
	Monkey(number=6, operation_fn=lambda x:x*11, divid_by=5 , to_true=7, to_false=4),
	Monkey(number=7, operation_fn=lambda x:x*x , divid_by=3 , to_true=4, to_false=2),
]


inspects = [0]*len(monkeys)
items = copy.deepcopy(items_default)
for i in range(20):
	for num in range(len(monkeys)):
		monkeys[num].inspect1()
print(inspects)
inspects.sort(reverse=True)
print(f'part1: {inspects[0] * inspects[1]}')
print()


inspects = [0]*len(monkeys)
items = copy.deepcopy(items_default)
#common_multiple = 23*19*13*17
common_multiple = 7*17*11*13*19*2*5*3
for i in range(10000):
	items = [[j%common_multiple for j in k] for k in items]
	for num in range(len(monkeys)):
		monkeys[num].inspect2()
print(inspects)
inspects.sort(reverse=True)
print(f'part2: {inspects[0] * inspects[1]}')

