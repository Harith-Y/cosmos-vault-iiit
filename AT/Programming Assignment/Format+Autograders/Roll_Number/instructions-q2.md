## Instructions for Question 2 Autograding

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
└── instructions-q1.md
└── instructions-q2.md
├── q1-p1-autograder.py
├── q1-p2-autograder.py
├── q1-p2.txt
└── q1-p2_sol.txt
├── q2-autograder.py
├── testcases.txt
└── testcases_sol.txt
```
You will be graded based on `q2.py` but the rest of the files are there so that you can test whether the solutions are read and stored correctly.

### Autograder for Question 2
```bash
python q2-autograder.py
Enter Input Dataset File Path:
testcases.txt
```
Your `q2.py` should produce an output file with the same name as the input testcase file (here `testcase.txt`), followed by `_output`. So for example in your test, the final file created should be `testcase_output.txt`

