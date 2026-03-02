
02/28/26

CS-350 Module Eight Portfolio Submission (Journal)
Selected Artifacts (2)

16x2 LCD Wiring + Display Bring-Up (Hardware + Interface Code)
Artifact shows my ability to correctly wire a parallel LCD (RS/EN/D4–D7) and initialize/display messages using Python libraries (digitalio, adafruit_character_lcd). 

README (1)

Raspberry Pi Embedded Thermostat (Integrated System Project)
Artifact shows a complete embedded system that combines GPIO output, PWM LEDs, interrupt-driven buttons, LCD output, I2C sensor input, and a state machine architecture. 

README (1)

Summary: What problem did this project solve?

This project solved the problem of building a working embedded thermostat on a Raspberry Pi by integrating multiple hardware peripherals and coordinating them through software. The thermostat reads temperature data from a sensor, displays information on the LCD, accepts user input from buttons, and visually indicates heating/cooling behavior using LEDs and PWM effects. 

README (1)

What did I do particularly well?

I did well at building the system progressively and validating each component step-by-step (GPIO → PWM → LCD → I2C sensor → buttons → state machine). This approach helped me isolate issues faster (especially wiring and pin numbering) and prevented one bug from breaking the entire project. 

README (1)

Where could I improve?

I could improve by adding more formal testing and logging, especially for hardware events (button presses, state changes, sensor read failures). I would also improve documentation by including a wiring diagram image and a short “troubleshooting” section (common pin mistakes, LCD contrast issues, etc.). (These are improvements beyond what’s currently written in the README.)

Tools and/or resources added to my support network

From this project, I added practical tools and resources that I can reuse in future embedded work:

Raspberry Pi GPIO + PWM development workflow

Adafruit CircuitPython libraries for LCD and sensors

Event-driven button handling (gpiozero.Button)

State machine structure for clean control logic 

README (1)

Transferable skills to other projects / coursework

The most transferable skills are:

Hardware/software integration (wiring + debugging + code)

Understanding communication methods (GPIO + I2C)

Event-driven programming using interrupts instead of constant polling 

README (1)

Designing systems using a state machine to keep behavior predictable and organized 

README (1)

How did I make it maintainable, readable, and adaptable?

I structured the project into clear phases and used separation of responsibilities (inputs like buttons/sensor, outputs like LCD/LEDs, and control logic in the thermostat state machine). This keeps the code easier to update (for example: adding a new “AUTO” mode later, changing the sensor type, or adjusting how often UART/LCD updates occur). 

README (1)

If you want, paste your file names for the two artifacts (example: lcd_wiring_notes.md, thermostat.py, etc.) and I’ll add a clean Repository Contents block under that section so it matches what’s actually in your GitHub.

Sources
projectreflect (1).docx
Document
Thermostat.py
Python
Thought for 6s

Perfect — I can use the two files you uploaded as your two portfolio artifacts:

Thermostat working code: Thermostat.py 

Thermostat

Final project reflection: projectreflect (1).docx 

projectreflect (1)

And I’ll also explicitly tie in your LCD wiring/bring-up using the exact GPIO pin mapping from your code (RS/EN/D4–D7). 

Thermostat

Below is a clean README section you can paste into your repo (I’d place it near the top, under your Project Overview).

CS 350 Module Eight Journal – Portfolio Submission
Selected Artifacts

LCD Wiring + Display Bring-Up (16x2 LCD over GPIO)

I successfully wired and initialized a 16x2 LCD using GPIO and the digitalio + adafruit_character_lcd libraries. The LCD uses RS=GPIO17, EN=GPIO27, and data pins D4=GPIO5, D5=GPIO6, D6=GPIO13, D7=GPIO26. 

Thermostat

This artifact demonstrates hands-on hardware integration and correctly mapping physical wiring to software pin configuration.

Thermostat Final Project (Full Embedded System Integration)

I designed and implemented a working thermostat on a Raspberry Pi using a state machine with three modes: OFF, HEAT, COOL. 

projectreflect (1)

The system integrates:

I2C sensor (AHTx0) for temperature readings 

projectreflect (1)

LCD output for time/temp/state display 

projectreflect (1)

Interrupt-driven buttons using gpiozero 

projectreflect (1)

PWM LEDs to visually show active heating/cooling behavior 

projectreflect (1)

UART serial output to send periodic status updates 

projectreflect (1)

Project Summary (What problem was it solving?)

This project solved the problem of building a complete embedded thermostat that can read real sensor data, respond to button input, present output on a 16x2 LCD, and indicate heating/cooling behavior with LEDs. The system combines multiple peripherals into one working application controlled by a clear state machine design. 

projectreflect (1)

What did I do particularly well?

I integrated multiple peripherals successfully (GPIO, PWM LEDs, LCD, I2C sensor, UART) and used an interrupt-driven approach for buttons, which improved responsiveness and avoided constant polling. 

projectreflect (1)

Where could I improve?

I could improve by adding more structured testing and debugging support (example: clearer error handling for sensor/UART failures, and adding logs that summarize state changes and readings). I would also add a wiring diagram image in the repository to make hardware setup faster for someone reproducing the build.

Tools/resources added to my support network

This project strengthened my support toolkit for embedded work:

Adafruit CircuitPython sensor libraries (AHTx0) 

projectreflect (1)

gpiozero for interrupt-style button handling 

projectreflect (1)

LCD libraries (digitalio, adafruit_character_lcd) 

projectreflect (1)

UART serial configuration and formatting for device-to-device output 

projectreflect (1)

Transferable skills

The most transferable skills from this project are embedded hardware/software integration, state machine architecture, interrupt-driven inputs, peripheral communication (I2C + UART), and writing modular code that can be expanded into larger IoT-style systems. 

projectreflect (1)

Maintainability / readability / adaptability

I made the project maintainable by organizing functionality into clear responsibilities (display handling, temperature reading, state machine logic, output control). The state machine structure keeps the behavior predictable and makes it easier to add future modes or swap sensors without rewriting the whole program. 

projectreflect (1)

Repository Files (Artifacts)

Thermostat.py — Final working thermostat program 

Thermostat

projectreflect (1).docx — Final project reflection write-up 

projectreflect (1)







02/24/26
# Raspberry Pi Embedded Thermostat Project

## Project Overview

This project represents the complete development of a Raspberry Pi–based embedded thermostat system built progressively from the ground up. Rather than starting with a finished design, this system was developed step-by-step throughout the course, beginning with basic GPIO wiring and expanding into a fully integrated multi-peripheral embedded system.

The final product integrates:

- GPIO digital output
- PWM LED control
- GPIO interrupt-driven buttons
- 16x2 LCD display
- I2C temperature sensor
- UART serial communication
- State machine architecture
- Multithreaded display management

This project demonstrates full embedded systems integration on a Linux-based ARM platform.

---

# Development Progression

## Phase 1 – Basic GPIO & LED Control

The project began with basic GPIO configuration on the Raspberry Pi.  

- Wired a single LED with a resistor to GPIO.
- Configured digital output using Python.
- Verified correct HIGH/LOW output behavior.
- Implemented PWM to fade the LED.

This phase introduced:
- GPIO pin numbering (BCM vs BOARD)
- Hardware wiring fundamentals
- Pulse Width Modulation concepts

---

## Phase 2 – LCD Display Integration

Next, a 16x2 character LCD was added.

- Wired 6 digital GPIO lines for RS, EN, D4–D7.
- Initialized LCD using `digitalio` and `adafruit_character_lcd`.
- Printed static messages.
- Implemented screen clearing and dynamic updates.

This phase reinforced:
- Parallel digital communication
- Hardware abstraction libraries
- Output device control

---

## Phase 3 – Temperature Sensor (I2C)

An AHTx0 temperature and humidity sensor was integrated via I2C.

- Initialized I2C bus using `board.I2C()`
- Communicated with sensor using Adafruit library
- Retrieved temperature data
- Converted Celsius to Fahrenheit

This introduced:
- I2C peripheral communication
- Serial bus protocols
- Data conversion logic

---

## Phase 4 – Dual LED State Indicators

Two LEDs were implemented to represent thermostat state:

- Red LED (Heating)
- Blue LED (Cooling)

Each LED uses PWM:
- Fade effect when actively heating/cooling
- Solid when temperature target reached

This demonstrated:
- Conditional hardware behavior
- PWM as visual system feedback
- Multi-output coordination

---

## Phase 5 – Button Interrupt Integration

Three push buttons were added:

- GPIO24 – Cycle thermostat state
- GPIO25 – Increase setpoint
- GPIO21 – Decrease setpoint

Buttons were configured using interrupt-based detection via `gpiozero.Button`.

This improved:
- Event-driven programming
- Interrupt handling
- User interaction design

---

## Phase 6 – State Machine Architecture

The thermostat was restructured using a formal state machine.

States:
- OFF
- HEAT
- COOL

Transitions:
- Cycle button rotates between states

State behavior:

OFF:
- All LEDs off

HEAT:
- If temperature < setpoint → Red LED fades
- Else → Red LED solid

COOL:
- If temperature > setpoint → Blue LED fades
- Else → Blue LED solid

This phase introduced:
- Structured system logic
- Deterministic state transitions
- Clean separation of responsibilities

---

## Phase 7 – UART Communication

The thermostat sends status updates every 30 seconds via UART:


Lessons Learned
This project reinforced the importance of:
Proper wiring and hardware debugging
Understanding pin numbering systems
Separating hardware logic from state logic
Using event-driven programming instead of polling
Designing modular, maintainable embedded code
Building this system progressively from individual components into a fully integrated thermostat strengthened my understanding of real-world embedded systems architecture.




-------------------------------------------------------------------



12/21/25

Pirate Intelligent Agent Project Reflection
Project Overview
In this project, I worked with a Jupyter Notebook that implemented a pirate intelligent agent using reinforcement learning. The starter code provided the environment setup, game logic, and structure needed to train an agent to navigate a grid and find treasure while avoiding obstacles. My work focused on completing and modifying the reinforcement learning components, including defining the state representation, action selection, reward handling, and training loop. I implemented and tuned a Deep Q-Learning approach using a neural network to help the agent learn optimal behavior over time through trial and error.
Connection to Computer Science
This project helped me better understand how reinforcement learning and neural networks are used to solve real-world problems in computer science. Computer scientists design, build, and improve systems that can process information, make decisions, and adapt over time. This matters because many modern technologies, such as autonomous systems, recommendation engines, and game AI, rely on these concepts. Through this project, I saw how abstract ideas like rewards, policies, and exploration can translate into intelligent behavior in a working system.
Problem-Solving Approach
As a computer scientist, I approach problems by breaking them down into smaller, manageable parts. In this project, that meant understanding the environment, defining how the agent perceives the world, choosing an appropriate learning strategy, and iterating on the solution through testing and adjustment. When the agent did not perform well, I analyzed training output, adjusted parameters like epsilon and learning rate, and reran experiments. This iterative process reinforced the importance of testing, debugging, and refining solutions based on evidence.
Ethical Responsibilities
This course also highlighted my ethical responsibilities as a developer. When creating intelligent systems, it is important to consider how decisions are made, how data is used, and how users may be affected. For this project, that means recognizing that reinforcement learning systems can develop unintended behaviors if rewards are poorly designed. In real-world applications, developers must prioritize transparency, fairness, and user safety while also meeting organizational goals. Responsible AI design helps build trust and ensures that technology benefits users rather than causing harm.



Mobile App Development – Weight Tracking App (Project Three)

App Requirements and Goals
The app I developed is a Weight Tracking App designed to help users monitor their daily weight progress toward a personal fitness goal. The primary user needs addressed include easy weight entry, visual progress feedback, and a clean, simple navigation structure to avoid overwhelming the user. By allowing users to track and reflect on their progress over time, the app supports healthy habit-building and personal goal motivation.

User-Centered Screens and Features
The main screens include:
Login Screen – secure access
Dashboard/Home Screen – displays current goal and recent tracking data
Daily Weight Entry Screen – quick input and confirmation
Progress View (Grid/List or Chart) – lets users visually review weight changes
During design, I followed Android design principles like large touch targets, consistent placement of navigation elements, and simple forms. The UI was successful because it reduced friction—users can add or view their weight in just a few taps.
Development Approach

I broke the development into manageable tasks: UI first, then data handling and interactions. I used incremental coding and testing after each feature to keep bugs small and easy to track. Additionally, organizing layouts and logic into separate components helped me maintain clean and readable code. This approach will definitely help in future projects, especially when adding new features or troubleshooting.
Testing for Functionality

To ensure functionality, I tested each screen individually and then tested navigation flows end-to-end. Input validation, screen orientation checks, and emulator/device testing helped catch issues early. Testing is essential because it reveals user experience problems and prevents errors from moving into later development stages where they are harder to fix.
Overcoming Challenges

One challenge I faced was aligning UI elements correctly across different screen sizes. I overcame it by using Android’s constraint layout system and checking multiple emulator sizes to confirm responsiveness. Another challenge was ensuring data flowed properly from screen to screen, which I solved by reviewing lifecycle methods and debugging step-by-step.
Strongest Component

I am particularly proud of how the progress display feature turned out. It demonstrates my understanding of layouts, user-friendly design, and data handling. It also shows my ability to create a feature that is both functional and motivational for the end user.




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



Artemis Financial Secure Software Project


Reflection on My Work
For this project, my client was Artemis Financial, a company that provides financial services and wanted to strengthen the security of its software systems. Their main concern was ensuring that customer financial data and transactions were protected from vulnerabilities. The issue they wanted me to address was identifying weaknesses in their codebase and applying secure coding practices to reduce the risk of exploitation.
One thing I did well was running a complete vulnerability assessment and carefully analyzing the results. I made sure to identify false positives and focus on the real issues that could affect the client’s security posture. Coding securely is important because it protects sensitive data, builds customer trust, and helps avoid costly breaches or downtime. Software security adds real value by keeping the company’s reputation strong and ensuring long-term stability.
The most challenging part of the assessment was sorting through the different vulnerability reports and deciding which issues were critical and which were less important. At the same time, it was also helpful because it gave me practice using industry tools and seeing firsthand how dependencies and misconfigurations can create risks. To increase layers of security, I implemented HTTPS, added certificate management, and used a suppression file to remove irrelevant warnings. In the future, I would continue using automated scanning tools, like OWASP Dependency-Check, along with manual code reviews to decide which mitigation techniques to apply.
To make sure the software was still functional after refactoring, I ran the application, tested its endpoints, and double-checked the build reports. After changes, I re-ran the vulnerability scan to confirm no new issues were introduced. I also followed best practices like modular code, proper documentation, and consistent formatting to reduce the chance of errors.
Some resources and tools I found especially useful were the OWASP Dependency-Check plugin for automated scans and Maven for managing project dependencies. Secure coding habits like validating input, using strong encryption, and commenting code clearly will help me in future projects.
If I were showing this assignment to a future employer, I would highlight both the Vulnerability Assessment Report and the refactored secure code. These artifacts show that I can identify security issues, apply industry-standard tools, and deliver a functional piece of software that is hardened against vulnerabilities. It’s a concrete example of my ability to balance functionality with security, which is a key skill in professional software development.
