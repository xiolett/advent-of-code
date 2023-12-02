import re
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
    
def transcribe_words_to_numbers(text: str) -> str:
    # Define a mapping of words to numbers
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Build a regular expression pattern from the dictionary keys
    # Regex Pattern: https://regex101.com/r/PElozL/1
    pattern = re.compile(
        '(?=(' + 
        '|'.join(re.escape(word) for word in word_to_number) +
        '))'
    )
    
    # Find all instances of keys in string
    matches = re.finditer(pattern, text)
    for match in matches:
        start, _ = match.span()  # Use span to find start position of match
        # Insert matched group(1) into string
        text = text[:start] + \
            word_to_number[match.group(1)] + \
                text[start+1:]
    
    return text
    

if __name__ == "__main__":
    f = open("./2023/day1/input.txt", "r")
    
    # Create an empty list to store double digits of calibration values
    calibration_values = []

    # Process each line of puzzle input
    for line in f:
        line = line.strip()
        
        mod_line = transcribe_words_to_numbers(line)
        print(f"Translated {line} to {mod_line}")
        
        # Then get digits!
        nums = get_digits(mod_line)
        print(f"Line's numberical characters in order are: '{nums}'")
        
        # Use string indices to form first and last digits
        double_digit = int(nums[0] + nums[-1])
        print(f"Double digit is: '{double_digit}'")
        
        # Add to list of calibration values
        calibration_values.append(double_digit)
    
    # Print finalized result!
    print(f"The sum of calibration of digits: {sum(calibration_values)}")
