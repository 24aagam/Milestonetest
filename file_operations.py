# 15. Write a Python module named file_operations.py with functions for reading, writing, and appending data to a file.


def read_file(file_path):
    """Read the contents of a file and return them as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"The file {file_path} does not exist."

def write_file(file_path, data):
    """Write data to a file, overwriting any existing content."""
    with open(file_path, 'w') as file:
        file.write(data)

def append_to_file(file_path, data):
    """Append data to a file."""
    with open(file_path, 'a') as file:
        file.write(data)

# Example usage:
if __name__ == "__main__":
    file_path = 'example.txt'

    # Write data to the file
    write_file(file_path, 'Hello, World!\n')

    # Append data to the file
    append_to_file(file_path, 'This is an appended line.\n')

    # Read the contents of the file
    content = read_file(file_path)
    print(content)
