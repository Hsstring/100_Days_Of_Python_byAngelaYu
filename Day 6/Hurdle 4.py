def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
