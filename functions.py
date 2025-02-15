def detect_wall(maze, current_position, direction):
    x, y = current_position
    if direction == 'up':
        return maze[x][y + 1] == 0
    elif direction == 'down':
        return maze[x][y - 1] == 0
    elif direction == 'left':
        return maze[x + 1][y] == 0
    else:  # direction == 'right'
        return maze[x - 1][y] == 0

def drive_forward(maze, current_position, direction, result):
    x, y = current_position
    if direction == 'up' and not detect_wall(maze, current_position, 'up'):
        current_position = (x, y + 1)
        result.append(current_position)
    elif direction == 'down' and not detect_wall(maze, current_position, 'down'):
        current_position = (x, y - 1)
        result.append(current_position)
    elif direction == 'left' and not detect_wall(maze, current_position, 'left'):
        current_position = (x + 1, y)
        result.append(current_position)
    elif direction == 'right' and not detect_wall(maze, current_position, 'right'):  # direction == 'right'
        current_position = (x - 1, y)
        result.append(current_position)
    return current_position

def turn_left(direction):
    if direction == 'up':
        return 'left'
    elif direction == 'down':
        return 'right'
    elif direction == 'left':
        return 'down'
    else:  # direction == 'right'
        return 'up'

def turn_right(direction):
    if direction == 'up':
        return 'right'
    elif direction == 'down':
        return 'left'
    elif direction == 'left':
        return 'up'
    else:  # direction == 'right'
        return 'down'
