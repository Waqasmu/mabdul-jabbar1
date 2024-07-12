#!/usr/bin/env python3
# Author ID: mabdul-jabbar1

def read_file_string(file_name):
    """
    Reads the content of a file and returns it as a string.
    
    Args:
    - file_name (str): Name of the file to read.
    
    Returns:
    - str: Content of the file as a string.
           Returns an error message if the file is not found.
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

def read_file_list(file_name):
    """
    Reads the content of a file and returns each line as a list element.
    
    Args:
    - file_name (str): Name of the file to read.
    
    Returns:
    - list: List where each element is a line from the file (stripped of newline characters).
            Returns an empty list if the file is not found.
    """
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        # Remove newline characters from each line
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

