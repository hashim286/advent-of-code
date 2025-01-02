import re


with open("example.txt") as file: 
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
        self.obstruction_coords: tuple[int, int] 
        self.obstructions_visited: dict[str, str] = {}
        self.loop_obstructions: list[tuple[int, int]] = []

    def move_to_start(self) -> str: 
        self.x_coord = self.x_coord_start
        self.y_coord = self.y_coord_start 
        self.direction = "north" 
        self.obstructions_visited = {}
        return "north"

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
        if (self.lines[self.x_coord][self.y_coord] == "#") or (self.x_coord == self.obstruction_coords[0] and self.y_coord == self.obstruction_coords[1]): 
            if self.obstructions_visited.get(f"{self.x_coord}|{self.y_coord}") is None: 
                self.obstructions_visited[f"{self.x_coord}|{self.y_coord}"] = [direction]
            else: 
                for impacted_direction in self.obstructions_visited.get(f"{self.x_coord}|{self.y_coord}"): 
                    if impacted_direction == direction: 
                        
                        self.loop_obstructions.append(self.obstruction_coords)
                        print(self.obstruction_coords)
                        self.obstructions_visited.get(f"{self.x_coord}|{self.y_coord}").append(direction)
                        print(self.obstructions_visited)
                        raise IndexError
                    
                self.obstructions_visited.get(f"{self.x_coord}|{self.y_coord}").append(direction)

            return True

        else: 
            return False

    def change_coords(self, direction: str, backwards: bool = False) -> None: 
        # undo our last movement to no longer be at the coordinates of the obstruction
        if backwards: 
            if direction == "north": 
                self.x_coord += 1
            elif direction == "east": 
                self.y_coord -= 1
            elif direction == "west": 
                self.y_coord += 1
            elif direction == "south": 
                self.x_coord -= 1

            return  

        # move forward normally
        if direction == "north": 
            self.x_coord -= 1

        elif direction == "east": 
            self.y_coord += 1

        elif direction == "west": 
            self.y_coord -= 1

        elif direction == "south": 
            self.x_coord += 1

    def create_loop(self, direction: str, x_coordinate: int, y_coordinate: int) -> str: 
        self.obstruction_coords = (x_coordinate, y_coordinate)                
        direction = self.move_forward(direction)
        return direction


def main(lines: list[str]) -> None: 
    # instantiate our guard object and save its starting direction 
    guard: Guard = Guard(lines)    
    direction: str = guard.direction
    for i in range(len(lines)): 
        for j in range(len(lines[0])):
            direction = guard.move_to_start()
            if i == guard.x_coord_start and j == guard.y_coord_start: 
                continue
            while True: 
                try: 
                    direction = guard.create_loop(direction, x_coordinate=i, y_coordinate=j)
                except IndexError: 
                    break 

#    print(len(guard.loop_obstructions))
#    print(guard.loop_obstructions)

main(lines)
