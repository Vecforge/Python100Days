# Hurdles race 3
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.

# The position and number of hurdles changes each time this world is reloaded.
# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

# Difficulty level

# Background image: www.pexels.com


# A robot located at (x, y) = (1, 1) carries no objects.
# Goal to achieve:
# The final position of the robot must be (x, y) = (13, 1)
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# ----------------------------Answer------------------------------

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