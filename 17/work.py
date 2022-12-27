import numpy as np

#rocks_number = 2022
rocks_number = 1000000000000

with open('input.txt') as f:
	data = list(f.readline())
#print(data)

Hbar = np.array([
	[0,0,1,1,1,1,0],
])
Cross = np.array([
	[0,0,0,1,0,0,0],
	[0,0,1,1,1,0,0],
	[0,0,0,1,0,0,0],
])
Lshape = np.array([
	[0,0,0,0,1,0,0],
	[0,0,0,0,1,0,0],
	[0,0,1,1,1,0,0],
])
Vbar = np.array([
	[0,0,1,0,0,0,0],
	[0,0,1,0,0,0,0],
	[0,0,1,0,0,0,0],
	[0,0,1,0,0,0,0],
])
Block = np.array([
	[0,0,1,1,0,0,0],
	[0,0,1,1,0,0,0],
])
Space = np.array([
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
])
Floor = np.array([
	[1,1,1,1,1,1,1],
])
Tower = np.vstack([Space, Floor])
#print('Hbar:\n'  , Hbar  )
#print('Cross:\n' , Cross )
#print('Lshape:\n', Lshape)
#print('Vbar:\n'  , Vbar  )
#print('Block:\n' , Block )
#print('Space:\n' , Space )
#print('Floor:\n' , Floor )
#print('Tower:\n' , Tower )
rocks_order  = [Hbar, Cross, Lshape, Vbar, Block]



def move_rock_x(tower, rock, step, jet):
	rock_x = rock.shape[0]
	rock_y = rock.shape[1]
	zeros = np.zeros((rock_x, rock_y))
	tower_mod = np.vstack([zeros, tower])

	if jet == '>':
		if 1 in rock[:,-1]:
			rock_next = rock
		else:
			rock_next = np.roll(rock, 1)
	elif jet == '<':
		if 1 in rock[:,0]:
			rock_next = rock
		else:
			rock_next = np.roll(rock, -1)
	else:
		raise Exception('Error!')

	if (2 in rock_next + tower_mod[step:step+rock_x,:]):
		rock_next = rock

	return rock_next


def build_tower(tower, rock, step):
	rock_x = rock.shape[0]
	rock_y = rock.shape[1]
	zeros = np.zeros((rock_x, rock_y))
	tower_mod = np.vstack([zeros, tower])
	isStopped = False

	tower_next = tower
	if (2 in rock + tower_mod[step+1:step+rock_x+1,:]):
		tower_mod[step:step+rock_x,:] += rock
		tower_mod = np.where(tower_mod==0, 0, 1)
		tower_mod = tower_mod[~np.all(tower_mod==0, axis=1), :]
		tower_mod = np.vstack([Space, tower_mod])
		tower_next = tower_mod
		isStopped = True

	return tower_next, isStopped


def resize_tower(tower, bingo_index):
	tower_next = tower[:bingo_index+1,:]
	bingo_tall = len(tower)-(bingo_index+1)
#	print(tower_next, bingo_tall)
	return tower_next, bingo_tall


i = 0
j = 0
tower_tall = 0
isCompleted = False
while isCompleted==False:
	for rock in rocks_order:
		j+=1
		if j>rocks_number:
			isCompleted = True
			break
		isStopped = False
		step = 0
		rock_next = rock
		while isStopped==False:
			jet = data[i%len(data)]
			rock_next = move_rock_x(tower=Tower, rock=rock_next, step=step, jet=jet)
			tower_next, isStopped = build_tower(tower=Tower, rock=rock_next, step=step)
			Tower = tower_next

			bingo_index_list = np.where(np.all(Tower==1, axis=1))[0]
			if len(bingo_index_list) > 1:
				bingo_index = bingo_index_list[0]
				Tower, bingo_total = resize_tower(tower=Tower, bingo_index=bingo_index)
				tower_tall += bingo_total

			step+=1
			i+=1

Tower = Tower[~np.all(Tower==0, axis=1), :]

#print(Tower)
print(len(Tower)-1)
print(tower_tall+len(Tower)-1)
