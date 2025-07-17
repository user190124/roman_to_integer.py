# roman_to_integer.py
The program converts a Roman numeral string to an integer. The test cases cover all specified scenarios systematically. The program outputs the results of each test case, indicating whether it passes or fails based on the expected output.
The program converts a Roman numeral string to an integer, following these rules:

Roman Numerals: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
Subtractive Notation: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900.
Validations: Handles invalid letters, illegal repetitions (e.g., VV, IIII), and null inputs by returning 0.
Algorithm:

Check for null/empty input and return 0.
Define a dictionary mapping Roman numerals to their integer values.
Iterate through the string from right to left:
If the current numeral's value is greater than or equal to the previous, add it to the result.
If less, subtract it (handles subtractive notation like IV).
Validate for illegal repetitions (e.g., more than three I, X, C, or more than one V, L, D).
Return the final integer or 0 for invalid inputs.
Test Cases:
The test cases cover all specified scenarios systematically:

Single Letters: I (1), V (5), X (10), L (50), C (100), D (500), M (1000).
Many Letters: XI (11), VIIસ
System: VII (7), XVI (16).

Subtractive Notation: IV (4), IX (9), XL (40), XC (90), CD (400), CM (900).
With and Without Subtractive Notation: XIV (14), MCMLIV (1954).
Repetition: II (2), III (3), XX (20).
First Number: I (1).
Invalid Letter: Z (0).
Invalid and Valid Letter: XIZ (0).
Not Valid (Repetitions): VV (0), IIII (0), LL (0), DD (0).
Null/Empty: "" (0).
The program outputs the results of each test case, indicating whether it passes or fails based on the expected output.
