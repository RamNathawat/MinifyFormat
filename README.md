# Code Formatter

## Overview
This Python script is designed to identify and format minified JavaScript and Python files within a specified directory. It utilizes `jsbeautifier` for JavaScript files and `autopep8` for Python files to improve readability by applying appropriate formatting.

## Features
- Detects and formats minified JavaScript (`*.js`) and Python (`*.py`) files.
- Logs detailed information about each formatted file, including time taken for formatting.
- Provides a summary of total files formatted and overall execution time upon completion.

## Requirements
- Python 3.x
- Libraries:
  - `jsbeautifier`
  - `autopep8`

## Usage
1. **Clone the Repository:**
   git clone <repository-url>
   cd Code_Formatter
Install Dependencies:
Ensure you have Python 3.x installed. Install required libraries:

pip install jsbeautifier autopep8
Run the Script:
Execute the script by providing the folder path containing minified code:

python main.py
Input Folder Path:
Enter the absolute or relative path of the folder containing minified JavaScript and Python files when prompted.

Output:
The script will format identified files and output detailed logs in the console.

Example
Suppose you have a directory minified_code containing minified JavaScript and Python files. Running the script on this directory will format these files for improved readability.

Notes
Ensure that the script has appropriate read and write permissions for the files within the specified directory.
Backup important files before running the script, as it will overwrite the existing files with formatted versions.
