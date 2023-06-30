import os
import sys


def merge_txt_files(folder_path, output_file):
    # Create an empty list to store the lines from all .txt files
    lines = []

    # Get the .txt files in the folder and sort them alphabetically
    txt_files = sorted([filename for filename in os.listdir(folder_path) if filename.endswith(".txt")])

    # Get the total number of .txt files
    total_files = len(txt_files)

    # Iterate over the sorted .txt files
    for i, filename in enumerate(txt_files):
        file_path = os.path.join(folder_path, filename)

        # Read each line from the current .txt file
        with open(file_path, "r") as file:
            file_lines = file.readlines()

        # Filter out empty lines and lines containing only numbers
        filtered_lines = [line for line in file_lines if line.strip() and not line.strip().isdigit()]

        # Extend the main list with the filtered lines
        lines.extend(filtered_lines)

        # Print progress
        print(f"Processing file {i+1}/{total_files}: {filename}")

    # Write the merged lines to the output file
    with open(output_file, "w") as output:
        output.writelines(lines)


# Check if the folder path argument is provided
if len(sys.argv) < 2:
    print("Please provide the folder path as an argument.")
    sys.exit(1)

# Get the folder path from the command-line argument
folder_path = sys.argv[1]

# Specify the output file name
output_file = "merged.txt"

# Merge the .txt files
merge_txt_files(folder_path, output_file)

print(f"\nFiles merged successfully. Merged content is stored in '{output_file}'.")
