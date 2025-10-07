## Instructions for Question 1 Autograding

**NOTE**
The example for Parts 1,2 are according to the assignment pdf. These scripts are for testing IO only and to show how the actual grading flow will happen.

This is how initially the folder structure should look like:
```bash
.
├── Question-1
│ ├── construct.py
│ └── predictions.py
├── Question-2
│ └── q2.py
├── dataset.txt
├── README.md
```
After Placing the autograder, the folder structure would look like:
```bash
.
├── Question-1
│ ├── construct.py
│ └── predictions.py
├── Question-2
│ └── q2.py
├── dataset.txt
├── dataset_sol.txt
├── instructions-q1.md
├── q1-p1-autograder.py
├── q1-p2-autograder.py
├── q1-p2.txt
└── q1-p2_sol.txt
```
You will be graded based on `construct.py` and `predictions.py` but the rest of the files are there so that you can test whether the solutions are read and stored correctly.

### Autograder for Question 1 Part 1
```bash
python q1-p1-autograder.py
Enter Input Dataset File Path:
dataset.txt
```

Your `construct.py` should produce an output file with the same name as the input dataset file (here `dataset.txt`), followed by `_output`. So for example in your test, the final file created should be `dataset_output.txt`
tldr;
The autograder will basically check whether your output file (`dataset_output.txt`) matches the solution file (`dataset_sol.txt`).

### Autograder for Question 1 Part 2
```bash
python q1-p2-autograde.py
Enter Input Dataset File Path:
q1-p2.txt
```
Your `predictions.py` should produce an output file with the same name as the input dataset file (here `q1-p2.txt`), followed by `_output`. So for example in your test, the final file created should be `q1-p2_output.txt`
tldr;
The autograder will basically check whether your output file (`q1-p2_output.txt`) matches the solution file (`q1-p2_sol.txt`).

## Note
- Please do not try to hardcode any paths as we would be having different folder structures for testing.
- You could assume that if all the testcases pass, your output files are in the correct format as expected.
- More details on Q2 autograder will be announced soon.
- Your solution python scripts should essentially take in the input file as an argument and store the required output in its corresponding text file.
- **Important**: Make sure that you follow the boilerplate given (`construct.py`, `predictions.py`) to handle IO.
- Make sure to end all lines with the newline character (including the last line).
