# File Read & Write with Error Handling

def modify_content(content):
    # This function modifies the content; for now, let's convert it to uppercase
    return content.upper()

def read_and_write_file():
    # Ask user for input file name
    input_filename = input("Enter the name of the file to read from: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nOriginal content read successfully.\n")

        # Modify the content
        modified_content = modify_content(content)

        # Ask user for output file name
        output_filename = input("Enter the name of the new file to write to: ")

        # Write modified content to new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"\nModified content has been written to '{output_filename}'.\n")

    except FileNotFoundError:
        print(f"\nError: File '{input_filename}' was not found.")
    except IOError:
        print(f"\nError: Could not read from or write to file.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Run the program
read_and_write_file()
