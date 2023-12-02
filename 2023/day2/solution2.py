from functools import reduce
import operator
import re

cube_color_set = {"red", "green", "blue"}

cube_set_inquiry = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# The power of a set of cubes is equal to the numbers of red, green, and 
# blue cubes multiplied together.
# Get the max value for each color's draws, then multiply to derive the power
def get_power_of_each_color(draws: dict) -> list[int]:
    
    return reduce(operator.mul, (
        max(value) for value in draws.values()
        )
                  )

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

    powers = []
    
    f = open("./2023/day2/input1.txt", "r")
    
    for line in f:
        print(f"Original Input: '{line.strip()}'")
        
        draw_dict = get_cube_draws_by_color(line)
        
        power = get_power_of_each_color(draw_dict)
        print(f"\tPower == {power}")
        
        powers.append(power)  
            
    print(sum(powers))
        
    
    
