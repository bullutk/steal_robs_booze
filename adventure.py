import random

print 'Whats up fool, what is your name?'
my_name = raw_input()


def msg(room):
	if room['msg'] == '':
		return "You have entered the " + room['name'] + '.'
	else:
		return room['msg']

def get_choice(room,dir):
	if dir=='N':
		choice=0
	elif dir=='E':
		choice=1
	elif dir=='S':
		choice=2
	elif dir=='W':
		choice=3
	else:
		return -1

	if room['directions'][choice]==0:
		return 4
	else:
		return choice

def main():
	dirs=(0,0,0,0)

	entrance={'name':'Entrance Way', 'directions':dirs, 'msg':''}
	livingroom={'name':'Living Room', 'directions':dirs, 'msg':''}
	hallway={'name':'Hallway', 'directions':dirs, 'msg':''}
	kitchen={'name':'Kitchen', 'directions':dirs, 'msg':''}
	diningroom={'name':'Dining Room', 'directions':dirs, 'msg':''}
	familyroom={'name':'Family Room', 'directions':dirs, 'msg':''}

	# directions: rooms to the (N,E,S,W)
	entrance['directions']=(kitchen,livingroom,0,0)
	livingroom['directions']=(diningroom,0,0,entrance)
	hallway['directions']=(0,kitchen,0,familyroom)
	kitchen['directions']=(0, diningroom,entrance,hallway)
	diningroom['directions']=(0,0,livingroom,kitchen)
	familyroom['directions']=(0,hallway,0,0)

	# place the basket in a random room
	rooms=[livingroom,hallway,kitchen,diningroom,familyroom]
	room_with_booze=random.choice(rooms)
	booze_snatched=False
	room=entrance

	print 'Welcome, ' + my_name + '! Can you find where Rob has stashed his booze?'

	while True:
		if booze_snatched and room['name']=='Entrance Way':
			print 'Congtrats ' + my_name + '! You have snatched the booze and retruned to the main entrance. Now go get drunk!'
			break
		elif not booze_snatched and room['name']==room_with_booze['name']:
			booze_snatched=True
			print(msg(room) + " There's the booze and Rob is passed out right next to it! You have grabbed the booze, now get out quick!")
			room['msg']='You are back in the ' + room['name']

		stuck=True

		while stuck:
			dir = raw_input("Which direction to you want to go? You can go N, S, E, or W.")
			choice = get_choice(room,dir)
			if choice == -1:
				print("You can only go N, S, E, or W")
			elif choice == 4:
				print("You cannot go in that direction.")
			else:
				room = room['directions'][choice]
				stuck = False

main()



















