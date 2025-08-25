def read_and_modify_file():
    """Read a file, modify its content, and write to a new file with error handling."""
    
    # Ask user for filename
    filename = input("Enter the filename to read: ")
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            
        print(f"Successfully read from '{filename}'")
        print(f"Original content: {content}")
        
        # Modify the content (convert to uppercase in this example)
        modified_content = content.upper()
        
        # Create new filename for the modified content
        if '.' in filename:
            name, ext = filename.rsplit('.', 1)
            new_filename = f"{name}_modified.{ext}"
        else:
            new_filename = f"{filename}_modified"
        
        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            
        print(f"Successfully wrote modified content to '{new_filename}'")
        print(f"Modified content: {modified_content}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        print("Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        print("You might need to change file permissions or run the program as administrator.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the contents of '{filename}'. It may be a binary file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Create the example.txt file with the specified content
def create_example_file():
    """Create an example file for testing."""
    with open("example.txt", "w") as file:
        file.write("God is good all the time")
    print("Created example.txt with content: 'God is good all the time'")

# Run the program
if __name__ == "__main__":
    # Create the example file first
    create_example_file()
    print("\n" + "="*50)
    
    # Run the main program
    read_and_modify_file()
