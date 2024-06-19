# File Creation and Writing
def create_and_write_file():
    try:
        # Open file in write mode ('w')
        with open('my_file.txt', 'w') as f:
            # Write three lines of text
            f.write("This is line 1\n")
            f.write("12345\n")
            f.write("Python is awesome!\n")
        print("File 'my_file.txt' created and initial content written successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # 
        pass

# File Reading and Display
def read_and_display_file():
    try:
        # Open file in read mode ('r')
        with open('my_file.txt', 'r') as f:
            # Read and print each line
            for line in f:
                print(line.strip())  # Strip newline character for clean output
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# File Appending
def append_to_file():
    try:
        # Open file in append mode ('a')
        with open('my_file.txt', 'a') as f:
            # Append three lines of text
            f.write("Appending line 1\n")
            f.write("98765\n")
            f.write("Appending more text!\n")
        print("Successfully appended to 'my_file.txt'.")
    except IOError as e:
        print(f"Error appending to file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        
        pass

# Error Handling
def main():
    try:
        create_and_write_file()
        print("\nFile content:")
        read_and_display_file()
        append_to_file()
        print("\nUpdated file content:")
        read_and_display_file()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Script execution complete.")

# Entry point of the script
if __name__ == "__main__":
    main()
