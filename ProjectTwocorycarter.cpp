// ProjectTwo.cpp
// Author: Cory Carter
// Date: June 23, 2025
//
// ABCU Course Planner
// This command-line program loads course information from a CSV file into
// an in‑memory data structure, provides an alphabetically sorted listing of
// courses, and allows users to query individual courses for their titles and
// prerequisites.
//
// The program expects each line of the CSV to have the following format:
//   COURSE_NUMBER,COURSE_TITLE[,PREREQ_1,PREREQ_2,...]
//
// Example:
//   CSCI100,Introduction to Computer Science
//   CSCI200,Data Structures,CSCI100
//
// Build instructions (g++ example):
//   g++ -std=c++17 -o CoursePlanner ProjectTwo.cpp
//
// ---------------------------------------------------------------------------

#include <algorithm>
#include <cctype>
#include <exception>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

struct Course {
    std::string number;
    std::string title;
    std::vector<std::string> prerequisites;
};

// Trim whitespace from both ends of a string.
static inline std::string trim(const std::string& str) {
    size_t first = str.find_first_not_of(" \t\r\n");
    if (first == std::string::npos) {
        return "";
    }
    size_t last = str.find_last_not_of(" \t\r\n");
    return str.substr(first, (last - first + 1));
}

// Convert string to uppercase (for case‑insensitive comparisons).
static inline std::string toUpper(std::string s) {
    std::transform(s.begin(), s.end(), s.begin(),
                   [](unsigned char c) { return std::toupper(c); });
    return s;
}

// Parse a line from the CSV file into a Course object.
Course parseLine(const std::string& line) {
    std::stringstream ss(line);
    std::string token;

    // Course number
    if (!std::getline(ss, token, ',')) {
        throw std::runtime_error("Missing course number.");
    }
    Course course;
    course.number = trim(toUpper(token));

    // Course title
    if (!std::getline(ss, token, ',')) {
        throw std::runtime_error("Missing course title.");
    }
    course.title = trim(token);

    // Prerequisites (if any remaining tokens)
    while (std::getline(ss, token, ',')) {
        std::string prereq = trim(toUpper(token));
        if (!prereq.empty()) {
            course.prerequisites.push_back(prereq);
        }
    }

    return course;
}

// Load courses from the specified CSV file into the provided map.
void loadCourses(const std::string& filename,
                 std::unordered_map<std::string, Course>& courses) {
    std::ifstream infile(filename);
    if (!infile.is_open()) {
        throw std::runtime_error("Unable to open file '" + filename + "'.");
    }

    std::string line;
    size_t lineNumber = 0;
    while (std::getline(infile, line)) {
        ++lineNumber;
        if (trim(line).empty()) {  // skip blank lines
            continue;
        }
        try {
            Course course = parseLine(line);
            courses[course.number] = std::move(course);
        } catch (const std::exception& e) {
            std::cerr << "Error parsing line " << lineNumber << ": " << e.what()
                      << std::endl;
        }
    }
}

// Print courses in alphanumeric order by course number.
void printCourseList(const std::unordered_map<std::string, Course>& courses) {
    if (courses.empty()) {
        std::cout << "No courses loaded. Please load data first.\n";
        return;
    }

    std::vector<const Course*> sortedCourses;
    sortedCourses.reserve(courses.size());
    for (const auto& kv : courses) {
        sortedCourses.push_back(&kv.second);
    }

    std::sort(sortedCourses.begin(), sortedCourses.end(),
              [](const Course* a, const Course* b) {
                  return a->number < b->number;
              });

    std::cout << "Here is a sample schedule:\n";
    for (const Course* c : sortedCourses) {
        std::cout << c->number << ", " << c->title << '\n';
    }
}

// Print information for a single course (number + title + prerequisites).
void printSingleCourse(const std::unordered_map<std::string, Course>& courses) {
    if (courses.empty()) {
        std::cout << "No courses loaded. Please load data first.\n";
        return;
    }

    std::cout << "What course do you want to know about? ";
    std::string input;
    std::cin >> input;
    input = toUpper(trim(input));

    auto it = courses.find(input);
    if (it == courses.end()) {
        std::cout << "Course '" << input << "' not found.\n";
        return;
    }

    const Course& c = it->second;
    std::cout << c.number << ", " << c.title << '\n';
    if (c.prerequisites.empty()) {
        std::cout << "Prerequisites: None\n";
    } else {
        std::cout << "Prerequisites: ";
        for (size_t i = 0; i < c.prerequisites.size(); ++i) {
            std::cout << c.prerequisites[i];
            if (i + 1 < c.prerequisites.size()) std::cout << ", ";
        }
        std::cout << '\n';
    }
}

// Display the main menu.
void printMenu() {
    std::cout << '\n'
              << "1. Load Data Structure.\n"
              << "2. Print Course List.\n"
              << "3. Print Course.\n"
              << "9. Exit\n";
}

// Program entry point.
int main() {
    std::unordered_map<std::string, Course> courses;
    bool exitProgram = false;

    std::cout << "Welcome to the course planner.\n";

    while (!exitProgram) {
        printMenu();
        std::cout << "What would you like to do? ";
        int choice;
        if (!(std::cin >> choice)) {
            std::cin.clear();                       // clear failure bits
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid input. Please enter a number.\n";
            continue;
        }

        switch (choice) {
            case 1: {
                std::cout << "Enter file name: ";
                std::string filename;
                std::cin >> filename;
                try {
                    loadCourses(filename, courses);
                    std::cout << "Data loaded successfully (" << courses.size()
                              << " courses).\n";
                } catch (const std::exception& e) {
                    std::cout << "Error: " << e.what() << '\n';
                }
                break;
            }
            case 2:
                printCourseList(courses);
                break;
            case 3:
                printSingleCourse(courses);
                break;
            case 9:
                std::cout << "Thank you for using the course planner!\n";
                exitProgram = true;
                break;
            default:
                std::cout << choice << " is not a valid option.\n";
        }
    }

    return 0;
}
