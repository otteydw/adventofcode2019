#!/usr/bin/python3

# https://adventofcode.com/2019/day/3

# --- Day 3: Crossed Wires ---
# The gravity assist was successful, and you're well on your way to the Venus
# refuelling station. During the rush back on Earth, the fuel management system
# wasn't completely installed, so that's next on the priority list.

# Opening the front panel reveals a jumble of wires. Specifically, two wires are
# connected to a central port and extend outward on a grid. You trace the path
# each wire takes as it leaves the central port, one wire per line of text (your
# puzzle input).

# The wires twist and turn, but the two wires occasionally cross paths. To fix
# the circuit, you need to find the intersection point closest to the central
# port. Because the wires are on a grid, use the Manhattan distance for this
# measurement. While the wires do technically cross right at the central port
# where they both start, this point does not count, nor does a wire count as
# crossing with itself.

## A taxicab geometry is a form of geometry in which the usual distance function
## or metric of Euclidean geometry is replaced by a new metric in which the
## distance between two points is the sum of the absolute differences of their
## Cartesian coordinates.

# For example, if the first wire's path is R8,U5,L5,D3, then starting from the
# central port (o), it goes right 8, up 5, left 5, and finally down 3:

# ...........
# ...........
# ...........
# ....+----+.
# ....|....|.
# ....|....|.
# ....|....|.
# .........|.
# .o-------+.
# ...........
# Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

# ...........
# .+-----+...
# .|.....|...
# .|..+--X-+.
# .|..|..|.|.
# .|.-X--+.|.
# .|..|....|.
# .|.......|.
# .o-------+.
# ...........
# These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

# Here are a few more examples:

# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

# What is the Manhattan distance from the central port to the closest intersection?

class Wire():

    def __init__(self):
        self.coordinates = {'x': 0, 'y': 0}

    def alter_path(self, path):
        SEQUENCE = path.rstrip().split(',')

        for request in SEQUENCE:
            direction = request[0]
            distance = int(request[1:])

            if direction == 'U':
                self.coordinates['y'] += distance
            elif direction == 'D':
                self.coordinates['y'] -= distance
            elif direction == 'L':
                self.coordinates['x'] -= distance
            elif direction == 'R':
                self.coordinates['x'] += distance
            else:
                print('Invalid direction!')
                exit(1)

    def get_coordinates(self):
        return self.coordinates


wire1 = Wire()
wire2 = Wire()

print(wire1.get_coordinates())
print(wire2.get_coordinates())

wire1.alter_path('R75,D30,R83,U83,L12,D49,R71,U7,L72')
wire2.alter_path('U62,R66,U55,R34,D71,R55,D58,R83')

print()
print(wire1.get_coordinates())
print(wire2.get_coordinates())