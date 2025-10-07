import os
import subprocess

def autograde(input_predictions_filepath):
    base, ext = os.path.splitext(input_predictions_filepath)
    output_filepath = f"{base}_output.txt"
    sol_filepath = f"{base}_sol.txt"

    if not os.path.exists(input_predictions_filepath):
        print(f"Error: Input file '{input_predictions_filepath}' not found.")
        return 0

    try:
        subprocess.run(
            ["python", "./Question-1/predictions.py", input_predictions_filepath],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: construct.py failed with exit code {e.returncode}")
        return 0

    if not os.path.exists(output_filepath):
        print(f"Error: Expected output file '{output_filepath}' not created.")
        return 0

    if not os.path.exists(sol_filepath):
        print(f"Error: Solution file '{sol_filepath}' not found.")
        return 0

    # check if solution file matches the produced output file
    solution_file = open(sol_filepath, "r")
    output_file = open(output_filepath, "r")

    sol_lines = solution_file.readlines()
    out_lines = output_file.readlines()

    if len(sol_lines) != len(out_lines):
        print(f"Error: Sol and out files have different number of lines")
        return 0

    correct_tokens = 0
    total_tokens = 0

    for i in range(len(sol_lines)):
        # [:-1] to remove the '\n'
        sol_line = sol_lines[i][:-1].split(' ')
        out_line = out_lines[i][:-1].split(' ')

        if len(sol_line) != len(out_line):
            print(f"Error: Sol and out files have different number of lines")
            return 0

        for j in range(len(sol_line)):
            if abs( float(sol_line[j]) - float(out_line[j])) < 10**(-5):
                correct_tokens += 1
            total_tokens += 1

    return int((correct_tokens / total_tokens) * 100)


print("Enter Predictions Input File Path:")
input_predictions_filepath = input()
score = autograde(input_predictions_filepath)
print(f"Input: {input_predictions_filepath}")
print(f"Score: {score}/100 points")
