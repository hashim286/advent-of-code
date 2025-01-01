import re


with open("data.txt") as file: 
    # read in the file and clean off \n character at the end of each item 
    lines: list[str] = file.readlines()
    lines: list[str] = [lines_cleaned.strip() for lines_cleaned in lines]

class Guard: 

    def __init__(self, lines): 
        # initialize the lines read in and a default direction of north, call the get_starting_position to find the initial coordinates
        self.lines = lines
        self.direction = "north"
        self.x_coord_start: int
        self.y_coord_start: int
        self.x_coord_start, self.y_coord_start = self.get_starting_position(self.lines)
        
        self.y_coord: int = self.y_coord_start
        self.x_coord: int = self.x_coord_start

        # if we hit an obstacle, we can use this to move back a direction
        self.new_direction: dict[str, str] = { 
                                              "north": "east", 
                                              "east": "south", 
                                              "south": "west", 
                                              "west": "north"
                                              }
        # this dictionary will keep track of every coordinate I have visited
        self.visited_coords: dict[str, bool] = {}

    def get_starting_position(self, lines: list[str]) -> tuple: 
    
        i: int
        for i in range(len(lines) - 1): 
            # searches for our guard ^ and returns a match object
            match_obj: re.Match = re.search(r"\^", lines[i])
            if type(match_obj) is re.Match: 
                line_match: int = match_obj.start()
                row_match: int = i
                # if we find a match, we return the i we are on and the first index of the match in the re object
                return  (row_match, line_match) 
            
    def move_forward(self, direction: str) -> str: 
        self.is_obstructed: bool = False 
        # breaks if it gets a "True" boolean indicating an obstruction or if the coordinates are less than 0 in either direction
        while not self.is_obstructed: 
            # if we get coordinates < 0 for either x or y, we raise an index error to break the loop as a negative index will go to the end of the list and add in negative indices which may have been visited but will be counted as new visits
            if self.x_coord < 0 or self.y_coord < 0: 
                raise IndexError

            # we query our dictionary that tracks our coordinates to see if there is already an entry, if so then we know we've been here before and can continue as normal, if not we add the new entry 
            if self.visited_coords.get(f"{self.x_coord}|{self.y_coord}") is None:
                self.visited_coords[f"{self.x_coord}|{self.y_coord}"] = True

            self.change_coords(direction) 
            self.is_obstructed = self.detect_obstruction(direction)

        # if we got here, it means there was some obstruction and so we must undo our last movement so we are no longer on the obstruction and also change our orientation 90 degrees clockwise
        self.change_coords(direction, backwards=True)
        self.direction = self.new_direction.get(direction)
        return self.direction
        

    def detect_obstruction(self, direction: str) -> bool: 
        # checks to see if the current character is an obstruction character and returns True if it is
        if self.lines[self.x_coord][self.y_coord] == "#": 
            return True

    def change_coords(self, direction: str, backwards: bool = False) -> None: 
        # undo our last movement to no longer be at the coordinates of the obstruction
        if backwards: 
            if self.direction == "north": 
                self.x_coord += 1
            elif self.direction == "east": 
                self.y_coord -= 1
            elif self.direction == "west": 
                self.y_coord += 1
            elif self.direction == "south": 
                self.x_coord -= 1

            return  

        # move forward normally
        if self.direction == "north": 
            self.x_coord -= 1

        elif self.direction == "east": 
            self.y_coord += 1

        elif self.direction == "west": 
            self.y_coord -= 1

        elif self.direction == "south": 
            self.x_coord += 1



def main(lines: list[str]) -> None: 
    # instantiate our guard object and save its starting direction 
    guard: Guard = Guard(lines)    
    direction: str = guard.direction
    while True: 
        try: 
            # for each direction return, we set the direction var to that new value and continue the loop 
            direction = guard.move_forward(direction)

        # index error is our break condition because if we try to move out of bounds in the +ve direction then we know we reached the end, if we move out of bounds in the -ve directon we will raise an error since we know we have reached the end that way 
        except IndexError: 
            break
    # prints the length of coords visited dictionary which counted each unique spot
    print(len(guard.visited_coords))


main(lines)
