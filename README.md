# ABCU Course Planner Portfolio

This repository contains two artifacts that demonstrate my skills in data structures and algorithms:

| Project | Artifact | Purpose |
|---------|----------|---------|
| **Project One – Data‑Structure Analysis** | `RuntimeAnalysis.docx` | Pseudocode, run‑time & memory analysis of Vector, Hash Table, and Binary Search Tree plus my design recommendation. |
| **Project Two – Course Planner Application** | `ProjectTwocorycarter.cpp` | Working command‑line tool that loads course data from a CSV file, prints the courses in alphanumeric order, and lets an adviser query a single course. |

---

## Reflection

### What was the problem you were solving in the projects for this course?
The Computer Science advising office needed a tool to help students plan their schedules. The software had to (1) ingest course data from a file, (2) list all courses alphabetically, and (3) display the details and prerequisites for any single course. Before writing code, I also evaluated three candidate data structures to decide which one would meet those requirements most efficiently.

### How did you approach the problem?
I compared Vectors, Hash Tables, and Binary Search Trees against the three core operations—load, sort, and search—using Big‑O analysis. After prototyping each structure, I chose a Binary Search Tree because it naturally maintains alphabetical order (so printing is fast) and still provides \(O(\log n)\) search time.

### How did you overcome any roadblocks you encountered?
Parsing lines that contained a variable‑length list of prerequisites was tricky at first. I fixed it by tokenizing each CSV line with `std::getline` and trimming whitespace. Another challenge was handling bad input files; I wrapped file I/O in `try`/`catch` blocks so the program fails gracefully and reports the exact line that caused trouble.

### How has your work on this project expanded your approach to designing software and developing programs?
I now prototype data structures and measure complexity **before** I commit to an implementation. That habit keeps me from rewriting large sections of code later.

### How has your work on this project evolved the way you write programs that are maintainable, readable, and adaptable?
The course planner follows a single‑responsibility style: loading, printing, and user‑interaction logic live in separate functions. I also added clear inline comments and formatted the code with consistent spacing, which will make future edits (like adding a GUI) much easier.

---

## Build & Run (Project Two)

```bash
g++ -std=c++17 -o CoursePlanner ProjectTwocorycarter.cpp
./CoursePlanner
```

The program will prompt for the CSV filename and then display a menu with options to load data, print the full course list, or query a single course.

---

## Repository Contents

```
.
├── ProjectTwocorycarter.cpp   # C++ source code
├── RuntimeAnalysis.docx       # Pseudocode + run‑time / memory study
└── README.md                  # You are here
```
