# Pythagorean Triplet Checker

This Python program helps identify whether a given set of numbers forms a Pythagorean triplet or not.

## Overview

The Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. This program checks if the entered values satisfy this condition.

## Installation

1. **Clone the repository:**
   
   **Termux:**
   ```bash
   pkg install git
   git clone https://github.com/SohelHaq/pythagorean-triplet-checker.git
   cd pythagorean-triplet-checker
   pip install -r requirement.txt
   python main.py
   ```
   **cmd**
    ```bash
    git clone https://github.com/SohelHaq/pythagorean-triplet-checker.git
    cd pythagorean-triplet-checker
    pip install -r requirement.txt
    ```
    **Linux:**
   ```bash
   apt install python python3 git -y
   git clone https://github.com/SohelHaq/pythagorean-triplet-checker.git
   cd pythagorean-triplet-checker
   pip install requirement.txt
   python main.py
   ```

3. **Install necessary dependencies:**

    Use the `requirements.txt` file to install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    **If It's not work use this**
   ```bash
    pip3 install -r requirements.txt
    ```
## Usage

To use this program:
1. Run the Python script `main.py`.
2. Follow the on-screen prompts to input values for 'a', 'b', and 'c'.
3. The program will determine if the provided values form a Pythagorean triplet or not.
4. It will display the result and necessary mathematical details.

## Sample Output

- For a Pythagorean triplet:
    ```bash
    Enter the value of a: 11
    Enter the value of b: 61
    Enter the value of c: 60

    Result:
	Question: (60,61,11)
	
	Answer:
		61² = 3721 ------- (1)
		60² + 11² = 3600 = 3721 ----- (2)
	
		∴ 61² = 60² + 11² ----- (from 1 & 2)
	The square of the largest number is equal to the 
	sum of the squares of the other two numbers.


    ```
- For values that do not form a Pythagorean triplet:
    ```bash
    Enter the value of a: 73
    Enter the value of b: 73
    Enter the value of c: 73

    Result:
	Question: (73,73,73)
	
	Answer:
		73² = 5329 ------- (1)
		73² + 73² = 5329 = 10658 ----- (2)
	
		∴ 73² ≠ 73² + 73² ----- (from 1 & 2)
	
	The square of the largest number is not equal to
	the sum of the squares of the other two numbers.
    ```

## Contribution

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
