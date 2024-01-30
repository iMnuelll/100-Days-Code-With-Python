'''
TRY THIS ON THE LINK : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_right() :
    turn_left()
    turn_left()
    turn_left()
while not at_goal() :
    if is_facing_north() and front_is_clear() :
        move()
    elif front_is_clear() :
        move()
    elif right_is_clear() and front_is_clear()  :
        move()
        turn_right()
    elif right_is_clear() and wall_in_front() :
        turn_right()
    elif right_is_clear() :
        turn_right()
    elif wall_in_front() :
        turn_left()
    elif wall_in_front() and wall_on_right() :
        turn_right()
'''
