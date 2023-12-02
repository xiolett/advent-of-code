import re

cube_color_set = {"red", "green", "blue"}

cube_set_inquiry = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_draw_valid(draws: dict) -> bool:
    # Cycle through inquiry color and max value of cubes
    for cube_color, max_cubes in cube_set_inquiry.items():
        # Check if current drawing for color is larger than inquiry
        if any(value > max_cubes for value in draws[cube_color]):
                return False
    # No need to return True until end
    return True
        

def get_cube_draws_by_color(input_str: str) -> list:
    # Initialize a dictionary with colors and empty lists
    # Don't use fromkeys() as all entries will share the same list reference >.>
    cube_draws = {key: [] for key in cube_color_set}
    
    pattern = re.compile(r"(\d+)\s(blue|red|green)")
    
    draws = re.findall(pattern, input_str)
    
    for draw in draws:
        print("\t\tDraw: ", draw)
        print(f"\t\tColor = {draw[1]}, Number = {draw[0]}")
        cube_draws[draw[1]].append(int(draw[0]))
        
    print(cube_draws)
    return cube_draws

if __name__ == "__main__":

    possible_game_ids = []
    game_id_pattern = r'\bGame (\d+)\b'
    
    f = open("./2023/day2/input1.txt", "r")
    
    for line in f:
        print(f"Original Input: '{line.strip()}'")
        
        game_id = int(re.search(game_id_pattern, line)[1])
        print(f"\tGame ID is: '{game_id}'")
        
        # TODO: See if you can do it without all loops :)
        draw_dict = get_cube_draws_by_color(line)
        
        is_valid = is_draw_valid(draw_dict)
        
        print(f"\tIs Game {game_id} Valid? {is_valid}")  
        
        if is_valid:
            possible_game_ids.append(game_id)
            
    print(sum(possible_game_ids))
        
    
    
