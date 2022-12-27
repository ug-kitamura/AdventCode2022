import numpy as np
import pandas as pd

data = np.loadtxt("input.txt", dtype='str')
data = [eval(i) for i in data]
data = list(set(data))
print(data)

df = pd.DataFrame(data=data, columns=['x', 'y', 'z'])
df = df.sort_values(by='x').sort_values(by='y').sort_values(by='z')
print(df)


def calc_x(x_map):
	area_count = 0
	if len(x_map) == 1:
		area_count = 6
	else:
		area_count = 6
		for i in range(len(x_map)-1):
			area_count += 6
			if abs(x_map[i]-x_map[i+1]) == 0:
				area_count -= 6
			elif abs(x_map[i]-x_map[i+1]) == 1:
				area_count -= 2
	return area_count

assert calc_x([1])==6
assert calc_x([1,2])==10
assert calc_x([1,2,3])==14
assert calc_x([1,2,4])==16


def calc_y(xy_map):
	area_count = 0
	y_list = [i for i in xy_map.keys()]
	for y in y_list:
		x_map = xy_map[y]
		area_count += calc_x(x_map)
	for i in range(len(y_list)-1):
		y1 = y_list[i]
		y2 = y_list[i+1]
		duplicate_x = set(xy_map[y1]) & set(xy_map[y2])
		area_count -= len(duplicate_x)*2
	return area_count

assert calc_y({2: [2]})==6
assert calc_y({1: [2], 2: [1, 2, 3], 3: [2]})==22
assert calc_y({1: [2], 2: [1, 2, 3], 3: [4]})==24
assert calc_y({1: [2], 2: [1, 3], 3: [2]})==24


def calc_z(xyz_map):
	area_count = 0
	z_list = [i for i in xyz_map.keys()]
	for z in z_list:
		xy_map = xyz_map[z]
		xy_df = pd.DataFrame(data=xy_map, columns=['x', 'y'])
		xy_df = xy_df.groupby('y')
		y_list = list(xy_df.groups.keys())
		xy_map_mod = {}
		for y in y_list:
			x_list = [i for i in xy_df.get_group(y)['x']]
			xy_map_mod[y] = x_list
		area_count += calc_y(xy_map_mod)
	for i in range(len(z_list)-1):
		z1 = z_list[i]
		z2 = z_list[i+1]
		duplicate_xy = set(xyz_map[z1]) & set(xyz_map[z2])
		area_count -= len(duplicate_xy)*2
	return area_count

assert calc_z({1: [(2, 2)], 2: [(2, 1), (1, 2), (2, 2), (3, 2), (2, 3)], 3: [(2, 2)], 4: [(2, 2)], 5: [(2, 1), (1, 2), (3, 2), (2, 3)], 6: [(2, 2)]})==64


def create_xyz_map(df):
	df = df.groupby('z')
	z_list = list(df.groups.keys())
	xyz_map = {}
	for z in z_list:
		xy_list = [tuple(i) for i in zip(df.get_group(z)['x'], df.get_group(z)['y'])]
		xyz_map[z] = xy_list
	print(xyz_map)
	return xyz_map


surface = calc_z(create_xyz_map(df))
print(f'part1: {surface} -> give up!')

