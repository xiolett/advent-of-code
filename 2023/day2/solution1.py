import re

cube_color_set = {"red", "green", "blue"}

cube_set_inquiry = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def get_cube_draws_by_color(input_str: str) -> list:
    # Initialize a dictionary with colors and empty lists
    # Don't use fromkeys() as all entries will share the same list reference >.>
    cube_draws = {key: [] for key in cube_color_set}
    
    pattern = re.compile(r"(\d+)\s(blue|red|green)")
    
    draws = re.findall(pattern, input_str)
    
    for draw in draws:
        print("Draw: ", draw)
        print(f"Color = {draw[1]}, Number = {draw[0]}")
        cube_draws[draw[1]].append(int(draw[0]))
        
    print(cube_draws)
    return cube_draws

if __name__ == "__main__":

    possible_game_ids = []
    game_id_pattern = r'\bGame (\d)\b'
    
    f = open("./2023/day2/example.txt", "r")
    
    for line in f:
        print(f"Original Input: '{line.strip()}'")
        
        game_id = re.search(game_id_pattern, line)[1]
        print(f"\tGame ID is: '{game_id}'")
        
        draw_dict = get_cube_draws_by_color(line)
        
        # TODO: logic on if game draws were possible for cube_set_inquiry
        
        
    
    
