# Hurdles race 1
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# What you need to know
# The functions move() and turn_left().
# Difficulty level

# More advanced
# You may have noticed that your solution has some repeated patterns. If you know how to define functions, define a function named jump() and use it to simplify your program.

# Difficulty level

# Background image: www.pexels.com


# A robot located at (x, y) = (1, 1) carries no objects.
# Goal to achieve:
# The final position of the robot must be (x, y) = (13, 1)

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

#--------------------Answer-----------------------

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