import numpy as np

data = np.loadtxt("input.txt", dtype='str')
print(data)


def snaf_to_decimal(snaf):
	decimal = 0
	snaf = list(snaf)
	snaf = snaf[::-1]
	for i,num in enumerate(snaf):
		if num.isdigit()==True:
			num = int(num)
		elif num=='-':
			num = -1
		elif num=='=':
			num = -2
		else:
			raise Exception('Error!')
		decimal += num*(5**i)
	return decimal

assert snaf_to_decimal('1=11-2')==2022
assert snaf_to_decimal('1-0---0')==12345
assert snaf_to_decimal('1121-1110-1=0')==314159265


def decimal_to_snafu(decimal):
	i = 0
	snaf = 0
	data = decimal
	while data!=0:
		digit = data%5
		snaf = snaf + digit * (10**i)
		data = data//5
		i = i+1
	snaf = list(str(snaf))
	snaf_reverse = snaf[::-1]
	snaf_reverse.append('x')
	for i in range(len(snaf)):
		if snaf_reverse[i]=='0':
			pass
		elif snaf_reverse[i]=='1':
			pass
		elif snaf_reverse[i]=='2':
			pass
		elif snaf_reverse[i]=='3':
			snaf_reverse[i] = '='
			if snaf_reverse[i+1]=='x':
				snaf_reverse[i+1] = '1'
			else:
				snaf_reverse[i+1] = str(int(snaf_reverse[i+1]) + 1)
		elif snaf_reverse[i]=='4':
			snaf_reverse[i] = '-'
			if snaf_reverse[i+1]=='x':
				snaf_reverse[i+1] = '1'
			else:
				snaf_reverse[i+1] = str(int(snaf_reverse[i+1]) + 1)
		elif snaf_reverse[i]=='5':
			snaf_reverse[i] = '0'
			if snaf_reverse[i+1]=='x':
				snaf_reverse[i+1] = '1'
			else:
				snaf_reverse[i+1] = str(int(snaf_reverse[i+1]) + 1)
		else:
			raise Exception('Error!')
	if snaf_reverse[-1] == 'x':
		snaf_reverse = snaf_reverse[:-1]
	snaf = ''.join(snaf_reverse[::-1])
	return snaf

assert decimal_to_snafu(2022)=='1=11-2'
assert decimal_to_snafu(12345)=='1-0---0'
assert decimal_to_snafu(314159265)=='1121-1110-1=0'


total_decimal = 0
for snaf in data:
	total_decimal += snaf_to_decimal(snaf)
print(total_decimal)

total_snaf = decimal_to_snafu(total_decimal)
print(f'part1: {total_snaf}')
