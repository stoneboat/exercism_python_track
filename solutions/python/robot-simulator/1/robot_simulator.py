# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction
    
    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                if self.direction == EAST:
                    self.direction = SOUTH
                elif self.direction == NORTH:
                    self.direction = EAST
                elif self.direction == WEST:
                    self.direction = NORTH
                elif self.direction == SOUTH:
                    self.direction = WEST
            if instruction == 'L':
                if self.direction == EAST:
                    self.direction = NORTH
                elif self.direction == NORTH:
                    self.direction = WEST
                elif self.direction == WEST:
                    self.direction = SOUTH
                elif self.direction == SOUTH:
                    self.direction = EAST
            if instruction == 'A':
                if self.direction == EAST:
                    self.coordinates = (self.coordinates[0]+1, self.coordinates[1])
                elif self.direction == NORTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1]+1)
                elif self.direction == WEST:
                    self.coordinates = (self.coordinates[0]-1, self.coordinates[1])
                elif self.direction == SOUTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1]-1)

