# Name: Rashneet Takhi
# Student ID: 12045112
# ICT105 Worksheet 2
# Advanced Network Security - Session 3 & 4
# Author: Tosh Revision: 2.0 Revision Date: 01 March 2026
# Completed: 2026-05-05

# =========================
# SESSION 2,3,4,
# =========================

# ===== QUESTION 1: LISTS BASIC =====
courses = [
    "Introduction to Programming",
    "Calculus I",
    "Microeconomics",
    "History I",
    "Psychology I",
    "Data Structures and Algorithms",
    "Physics I",
    "English Composition I",
    "Linear Algebra",
    "Chemistry I",
    "Biology I"
]

print("Original course list:")
print(courses)

# ===== QUESTION 2: SORTED() =====
print("\nAlphabetical order using sorted():")
print(sorted(courses))

print("\nReverse alphabetical order using sorted(..., reverse=True):")
print(sorted(courses, reverse=True))

print("\nOriginal list after sorted() calls:")
print(courses)

# ===== QUESTION 3: REVERSE() =====
print("\nUsing reverse() on a copy of the original list:")
courses_reversed = courses.copy()
courses_reversed.reverse()
print(courses_reversed)

print("\nReversing the copy again to restore order:")
courses_reversed.reverse()
print(courses_reversed)

# ===== QUESTION 4: SORT() =====
print("\nUsing sort() on a copy of the original list:")
courses_sorted = courses.copy()
courses_sorted.sort()
print(courses_sorted)

print("\nUsing sort(reverse=True) on the same copy:")
courses_sorted.sort(reverse=True)
print(courses_sorted)

# ===== QUESTION 5A: EXPRESSION OF INTEREST =====
sorted_courses = sorted(courses)
print("\nThe following courses are available for expression of interest if the students meet the prerequisites:")
for course in sorted_courses:
    print("-", course)

# ===== QUESTION 5B: REPLACE COURSE =====
courses_update = courses.copy()
withdrawn_course = "Biology I"
new_course = "Introduction to Philosophy"
index_to_replace = courses_update.index(withdrawn_course)

print("\nNOTICE:")
print(f"{withdrawn_course} has been withdrawn.")
print(f"It has been replaced by {new_course}.")

courses_update[index_to_replace] = new_course
print("\nOriginal course list:")
print(courses)
print("Updated course list:")
print(courses_update)

# ===== QUESTION 5C: ADD COURSES =====
print("\nAdding three new courses for this semester:")
courses_update.insert(0, "Calculus II")
courses_update.insert(len(courses_update) // 2, "Macroeconomics")
courses_update.append("Discrete Mathematics")

print("Updated course list with new courses:")
for course in courses_update:
    print("-", course)

# ===== QUESTION 5D: REMOVE COURSES =====
print("\nDue to technical and room availability issues, the following courses are unavailable:")
removed_courses = []
removed_courses.append(courses_update.pop())
removed_courses.append(courses_update.pop(0))
removed_courses.append(courses_update.pop(3))
removed_courses.append(courses_update.pop(2))

for course in removed_courses:
    print("-", course)

print("\nCourses still available this semester:")
for course in courses_update:
    print("-", course)

# ===== QUESTION 6: TUPLES AND LOOPS =====
course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I")
]

course_names = []
for course_id, course_name in course_tuples:
    course_names.append(course_name)

print("\nCourse names extracted from tuples:")
print(course_names)

# =========================
# SESSION 4
# =========================

# ===== QUESTION 7: CONDITIONAL STATEMENTS AND LOOPS =====
departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]

print("\n=== Department Finder ===")
while True:
    user_input = input("Enter course ID (1-15), 0, or quit: ")

    if user_input.lower() == "quit":
        print(f"The value {user_input} has been used to exit.")
        break

    if user_input == "0":
        print("Course ID is out of range (1-15), try again.")
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter an integer course ID, 0, or quit.")
        continue

    course_id = int(user_input)
    if 1 <= course_id <= 15:
        found = False
        for item in departments:
            if item[0] == course_id:
                print(f"Course ID {course_id} is in the {item[1]} department.")
                found = True
                break

        if not found:
            print(f"Course ID {course_id} is not found.")
    else:
        print(f"The value {course_id} has been used to exit.")
        break

# ===== QUESTION 8: COURSE INFORMATION RETRIEVAL SYSTEM =====
courses_data = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
]

user_input = input("\nEnter course ID to retrieve course information: ")

if user_input.isdigit():
    course_id = int(user_input)
    found = False
    for course in courses_data:
        if course[0] == course_id:
            print("\nCourse information:")
            print("Course ID:", course[0])
            print("Course Name:", course[1])
            print("Department:", course[2])
            print("Prerequisites:", course[3])
            found = True
            break

    if not found:
        print("Course ID not found. Please enter a number between 1 and 15.")
else:
    print("Invalid input. Please enter a valid integer course ID.")