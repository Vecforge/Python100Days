# Hurdles race 2
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
# What you need to know
# The functions move() and turn_left().
# The condition at_goal() and its negation.
# How to use a while loop.
# Your program should also be valid for world Hurdles 1.

# Difficulty level

# Background image: www.pexels.com


# A robot located at (x, y) = (1, 1) carries no objects.
# Goal to achieve:
# The final required position of the robot will be chosen at random.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# --------------------------Answer----------------------------

def h1():
    while not at_goal():
        if right_is_clear():
            turn_left()
            turn_left()
            turn_left()
            move()
        elif front_is_clear():
            move()
        
        if wall_in_front():
            turn_left()
            
        if is_facing_north() and not wall_on_right():
            turn_left()
            turn_left()
            turn_left()
            move()
h1()