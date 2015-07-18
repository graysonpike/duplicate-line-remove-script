import os
import sys


# Helper function
def removeDuplicates(lines):
    output = []
    used_lines = []

    for line in lines:
        used = False
        for used_line in used_lines:
            if line == used_line:
                used = True
        if not used:
            used_lines.append(line)
            output.append(line)

    return output


# USAGE:
# python3 filter.py <input filename> <output filename>

def main():
    # Ensure that the user has the correct number of arguments
    # otherwise, error message and quit()
    if(len(sys.argv) != 3):
        print("Usage: <input filename> <output_filename>")
        quit()

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    print("Removing duplicates from " + sys.argv[1] + ".")
    print("Output file is " + sys.argv[2])

    if not os.path.isfile(sys.argv[1]):
            raise Exception("Cannot find file: " + input_filename)

    temp = open(input_filename, "r")

    lines = temp.readlines()
    # Strip lines of newlines
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    # Remove duplicates
    lines = removeDuplicates(lines)

    temp.close()

    # 'w' setting creates a new file if it doesn't already exist.
    temp = open(output_filename, "w")
    for line in lines:
        temp.write(line + "\n")
    temp.close()

main()
