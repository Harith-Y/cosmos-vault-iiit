import sys
import os

if len(sys.argv) != 2:
    print("Usage: python q2.py '<input_path>'")
    sys.exit(1)

input_str = sys.argv[1]
input_file = open(input_str, "r")

'''
This is where you code your solution
'''

lines = ["Syntax Error\n", "No Error\n", "sadfasd Error\n"]

'''
Now store it in file
'''

base, ext = os.path.splitext(input_str)
output_file = open(f"{base}_output.txt", "w")
output_file.writelines(lines)
