with open('input.txt') as f:
	input = f.read()

#input = 'bvwbjplbdvbh' #5
#input = 'nppdvjthqldp' #6
#input = 'nznrnfrfntjf' #10
#input = 'zcfzfwzzqfrl' #11

#input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'    #19
#input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'      #23
#input = 'nppdvjthqldpwncqszvftbrmjlhg'      #23
#input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' #29
#input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'  #26

size = 4
#size = 14

i = size

while i < len(input):
	chars = input[i-size:i]

	if len(set(chars))==size:
		print(f"{i} : {chars}")
		break

	i = i + 1
