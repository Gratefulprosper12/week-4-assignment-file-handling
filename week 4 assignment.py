def file_processor():
    """Reads a file, processes its content, and writes to a new file with error handling."""
    
    # Get filename from user
    input_filename = input("Enter the filename to read: ")
    output_filename = input("Enter the output filename: ")
    
    try:
        # Read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        # Process the content (convert to uppercase in this example)
        modified_content = content.upper()
        
        # Write to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Success! Modified content written to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    file_processor()