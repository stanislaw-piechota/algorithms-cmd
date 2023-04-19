# Algorithms practice

## Overview
Python project with cmd/terminal context interactive menu. Created with `curses` in `Python 3.8+`

Application includes:
- submitting input
- running code
- checking input/output specification
- checking example code

## Navigation
Top line incldues information about module you're currently working on `ex. Factorialization, Options for Factorialization`

- To switch between options use **UP, DOWN ARROWS** or **W, S**
- To select option hit **ENTER**
- To go back to previous menu select **BACK** option
- To exit press **ESC**
- To leave top-level parts like code review hit any key

## Installation
1. Run terminal and change directory to main project folder
2. Install _curses_
    - For windows try `pip install windows-curses`
    - If it doesn't work and visit library website, download matching distribution _.whl_ and install it with `pip install <filename>`
    - Else, go to curses library website and download mathcing distribution and then `pip install <filename>`
3. Type in terminal `python main.py`

## Contributing
For the program to work it needs proper structure. Here are the rules your algorithm has to meet:

1. **Only one class** in file, both **named the same**
2. Class inherits from `processing.Module` and thus - has required methods
3. File is located in `algorithms` folder
4. There must be comments `# BEGIN` on the beginning of the algorithm and `# END` on the end of the algorithm
5. Don't duplicate categories, ex. Fibonacci series is included in section `Series` and doesn't need additional file