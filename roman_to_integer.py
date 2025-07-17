def roman_to_integer(s):
    if not s:  # Handle null or empty string
        return 0
    
    # Dictionary mapping Roman numerals to integers
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    # Iterate through the string from right to left
    for char in reversed(s):
        # Check if character is valid
        if char not in roman_values:
            return 0  # Invalid character returns 0
            
        curr_value = roman_values[char]
        
        # If current value is greater than or equal to previous, add it
        if curr_value >= prev_value:
            result += curr_value
        # If current value is less than previous, subtract it (handles subtractive notation)
        else:
            result -= curr_value
            
        prev_value = curr_value
    
    # Validate for illegal repetitions (e.g., VV, IIII)
    if any(s.count(char) > 3 for char in 'IXC') or \
       any(s.count(char) > 1 for char in 'VLD') or \
       'VV' in s or 'LL' in s or 'DD' in s:
        return 0
    
    return result

# Test cases
def run_tests():
    test_cases = [
        # Single letters
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        
        # Many letters
        ("XI", 11),
        ("VII", 7),
        ("XVI", 16),
        
        # Subtractive notation
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        
        # With and without subtractive notation
        ("XIV", 14),
        ("MCMLIV", 1954),
        
        # Repetition
        ("II", 2),
        ("III", 3),
        ("XX", 20),
        
        # First number
        ("I", 1),
        
        # Invalid letter
        ("Z", 0),
        
        # Invalid and valid letter
        ("XIZ", 0),
        
        # Not valid (repetitions)
        ("VV", 0),
        ("IIII", 0),
        ("LL", 0),
        ("DD", 0),
        
        # Null/empty
        ("", 0)
    ]
    
    for test_input, expected in test_cases:
        result = roman_to_integer(test_input)
        print(f"Input: {test_input}, Expected: {expected}, Got: {result}, "
              f"{'Pass' if result == expected else 'Fail'}")

# Run the tests
if __name__ == "__main__":
    run_tests()