from string import digits

# Creates constants for all the digits in the range 0 to 9.
# Converts lookup from O(n) to O(1)
digits = frozenset(digits)

def get_digits(text: str) -> str:
    """Consumes a single string variable and returns all number

    Args:
        text (str): String variable containing at least one digit. (example: "a1b2c3d4e5f")

    Returns:
        str: Returns string to avoid int overflow
    """
    
    if any(chr.isdigit() for chr in text):
        return ''.join(char for char in text if char in digits)
    else:
        return '0'

if __name__ == "__main__":
    f = open("./2023/day1/input.txt", "r")
    
    # Create an emprt list to store double digits of calibration values
    calibration_values = []

    # Process each line of puzzle input
    for line in f:
        print(f"Original line: '{line.strip()}'")
        
        nums = get_digits(line)
        print(f"Numbers in line in order are: '{nums}'")
        
        # Use string indices to form first and last digits
        double_digit = int(nums[0] + nums[-1])
        print(f"Double digit is: '{double_digit}'")
        
        # Add to list of calibration values
        calibration_values.append(double_digit)
    
    # Print finalized result!
    print(f"The sum of calibration of digits: {sum(calibration_values)}")
        
        
        