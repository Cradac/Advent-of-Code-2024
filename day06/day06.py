import copy

input = open(r"day06\\input.txt", "r")
map = input.read().split('\n')
map = [list(x) for x in map]

# remove empty line
map.remove([])

initial_map = copy.deepcopy(map)

VISITED_POSITIONS = []

# remember, it's [y,x]
MAP_X = len(map[0])
MAP_Y = len(map)
GUARD_LOCATION = [0,0]
GUARD_DIRECTION = 'up'
GUARD_ICON = '^'
DIRECTIONS = {
    'up': [-1, 0],
    'down': [1,0],
    'left': [0,-1],
    'right': [0,1]
}

# get initial coordiantes for guard
for i in range(len(map)):
    if '^' in map[i]:
        GUARD_LOCATION[0] = i
        GUARD_LOCATION[1] = map[i].index('^')

INITIAL_LOCATION = GUARD_LOCATION.copy()

def still_in_map():
    if -1 < GUARD_LOCATION[0] < MAP_Y or -1 < GUARD_LOCATION[1] < MAP_X:
        return True
    else:
        return False
    
def turn_right():
    global GUARD_DIRECTION, GUARD_ICON
    if GUARD_DIRECTION == 'up':
        GUARD_DIRECTION = 'right'
        GUARD_ICON = '>'
    elif GUARD_DIRECTION == 'right':
        GUARD_DIRECTION =  'down'
        GUARD_ICON = 'v'
    elif GUARD_DIRECTION == 'down':
        GUARD_DIRECTION = 'left'
        GUARD_ICON = '<'
    elif GUARD_DIRECTION == 'left':
        GUARD_DIRECTION = 'up'
        GUARD_ICON = '^'
    else:
        print(GUARD_DIRECTION)
        exit(1)

# return True if step before is free, if obstacle returns false
def lookahead(working_map):
    # this will fail if looking out of the map
    try:
        if working_map[GUARD_LOCATION[0]+DIRECTIONS[GUARD_DIRECTION][0]][GUARD_LOCATION[1]+DIRECTIONS[GUARD_DIRECTION][1]] =='#':
            return '#'
        else:
            return 'free'
    except:
        return 'oob'


def step():
    GUARD_LOCATION[0], GUARD_LOCATION[1] = GUARD_LOCATION[0]+DIRECTIONS[GUARD_DIRECTION][0], GUARD_LOCATION[1]+DIRECTIONS[GUARD_DIRECTION][1]

while still_in_map():
    VISITED_POSITIONS.append(GUARD_LOCATION.copy())
    if lookahead(map) == 'free':
        step()
        # set new marker
        map[GUARD_LOCATION[0]][GUARD_LOCATION[1]] = GUARD_ICON
    elif lookahead(map) == '#':
        turn_right()
        # set new marker
        map[GUARD_LOCATION[0]][GUARD_LOCATION[1]] = GUARD_ICON
    else: # oob
        break

print("Amount of distinctly visited positions: (Star #1)")
print(len(set(tuple(x) for x in VISITED_POSITIONS)))

def in_loop(visited_positions, guard_location, guard_direction):
    # check if guard has been at the same point with the same direction already
    #print(visited_positions)
    #print(guard_location, guard_direction)
    if (guard_location, guard_direction) in visited_positions:
        return True
    else:
        return False

# and then just literally place a box in every single location (of a dot, not barrier or starting position)
# and count the amount of time in_loop is returning true

permutations = len(map)*len(map[0])
print(f'going through ~{permutations} permutations...')

AMNT_OBSTR_POSITIONS = 0
COUNTER = 0

'''
for line in initial_map:
    print("".join(line))
print('')
'''

for y in range(len(initial_map)):
    for x in range(len(initial_map[0])):
        # try placing a box at every single position possible:
        if initial_map[y][x] == '#' or initial_map[y][x] == '^':
            COUNTER += 1
            continue
        map_copy = copy.deepcopy(initial_map)
        map_copy[y][x] = '#'
        
        '''
        for line in map_copy:
            print("".join(line))
        print('')
        '''

        # clean up
        VISITED_POSITIONS.clear()
        GUARD_LOCATION = INITIAL_LOCATION.copy()
        GUARD_DIRECTION = 'up'

        # logic here
        while still_in_map():
            VISITED_POSITIONS.append((GUARD_LOCATION.copy(), GUARD_DIRECTION))
            if lookahead(map_copy) == 'free':
                step()
            elif lookahead(map_copy) == '#':
                turn_right()
            else:
                # out of bounds
                COUNTER += 1
                break
            if in_loop(VISITED_POSITIONS, GUARD_LOCATION, GUARD_DIRECTION):
                AMNT_OBSTR_POSITIONS += 1
                COUNTER += 1
                break
        print(COUNTER, '/', permutations)

# Last result: 2096, too high

print("Amount of possible obstructions: (Star #2)")
print(AMNT_OBSTR_POSITIONS)