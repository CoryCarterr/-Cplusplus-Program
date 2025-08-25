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






README – CS330 Final Project


Reflection on My Design Approach
When I first started designing this project, I approached it like building something in layers. I wanted to get the basic shapes and layout in place first, then add details like lighting, textures, and camera movement. This step-by-step approach helped me stay organized instead of getting overwhelmed. One new design skill I developed was figuring out how to make small objects (like the basketball rim or table) feel part of a larger, believable scene. I realized that design isn’t just about making things look good—it’s about making them work together as a whole.
For my design process, I focused on testing ideas quickly. I would sketch out what I wanted, try it in code, and then refine it based on how it actually looked in the scene. This type of iteration gave me confidence that I could make steady progress instead of expecting everything to be perfect on the first try. These tactics—breaking big goals into smaller steps and testing frequently—are ones I know I can use in future courses and professional projects.
Reflection on My Development Approach
When it came to programming, I leaned on iteration even more. I would code a feature, run the program, see how it behaved, then go back and tweak it. This was especially true with lighting and collision logic. I also learned new strategies like modularizing my code so different pieces (objects, lighting, shaders) were easier to manage. Over the milestones, I definitely became more comfortable with debugging and reading error messages, which made the final project feel like a natural completion of everything I had been practicing.
My approach to development evolved a lot during this course. At first, I was just trying to get the code to compile. By the end, I was thinking about design choices, readability, and performance. That shift is something I’ll carry forward in future projects.
Computer Science and My Goals
Working on computational graphics has given me both technical and creative skills. From an educational standpoint, I now have hands-on experience with OpenGL, transformations, lighting, and collision detection—things that looked intimidating at first but now make sense after working through them. Professionally, I can see how these skills connect to areas like simulation, visualization, and even game development. Even if I don’t end up working in graphics directly, the problem-solving approach I practiced here applies to any software development role.
Overall, this project showed me how computer science isn’t just about solving technical problems—it can also be a way to express ideas visually. That combination of creativity and logic is exactly why I want to keep pushing forward in this field.
