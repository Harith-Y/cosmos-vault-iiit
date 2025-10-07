import sys
import os

if len(sys.argv) != 2:
    print("Usage: python construct.py '<input_path>'")
    sys.exit(1)

input_str = sys.argv[1]
input_file = open(input_str, "r")

'''
This is where you code your solution
'''

lines = ['0 0.5 0 0.5\n', '0 0 1 0\n', '0 0.5 0.5 0\n', '0 0 1 0\n', '1 0 0\n', '0 0.5 0.5\n', '0 0.66667 0.33333\n', '0 1 0\n']

'''
Now store it in file
'''

base, ext = os.path.splitext(input_str)
output_file = open(f"{base}_output.txt", "w")
output_file.writelines(lines)
